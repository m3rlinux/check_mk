#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import os
import sys

usage = """Run this script inside a OMD site
    Usage: ./wato_import.py csvfile.csv
    CSV Example:
        wato_foldername;hostname;host_alias;ipaddress;tag1 tag2 tag3 tag4"""

try:
    path = os.environ.pop('OMD_ROOT')
    pathlocal = path+"/etc/check_mk/conf.d/wato"
    pathlocal = os.path.expanduser(pathlocal)
    csv_file = open(sys.argv[1], 'r')
except:
    print(usage)
    sys.exit()

# elaborazione del file csv
folders = {}
for line in csv_file:
    if line.startswith('#'):
        continue
    if len(line.split(';')) != 5:
        print(usage)
        sys.exit()
    target_folder, name, alias, ipaddress, tags = line.split(';')
    if target_folder:
        try:
            os.makedirs(pathlocal + "/" + target_folder.lower())
        except os.error:
            pass
        folders.setdefault(target_folder, [])
        ipaddress = ipaddress.strip()
        if ipaddress == "None":
            ipaddress = False
        folders[target_folder].append((name, alias, ipaddress, tags))
csv_file.close()

# caricamento TAG da CheckMK
wato_tags = {}
host_tags_info = {"wato_aux_tags": [], "wato_tags": {}}
exec(open(pathlocal+"/../../multisite.d/wato/tags.mk").read())
host_tag_mapping = {}
aux_tag_mapping = {}
for tag_group in wato_tags['tag_groups']:
    for choice in tag_group['tags']:
        host_tag_mapping[choice['id']] = tag_group['id']
        aux_tag_mapping[choice['id']] = choice['aux_tags']

for folder in folders:
    all_hosts = ""
    ips = ""
    servers = {}
    folder_tags = {}
    for name, alias, ipaddress, tags in folders[folder]:
        real_name = name.strip()
        servers[real_name] = {}
        extra_infos = []
        # WATO Tag extra info
        host_aux_tags = set()
        host_tags = []
        if len(tags) > 1:
            for tag in tags.split():
                host_aux_tags |= set(aux_tag_mapping.get(tag, []))
                if tag not in host_tag_mapping:
                    print("Unknown host tag: %s" % tag)
                else:
                    servers[real_name].update({'tag_' + host_tag_mapping[tag]: tag})

        extra_aux_tags = ""
        if host_aux_tags:
            extra_aux_tags = "|".join(host_aux_tags) + "|"
        all_hosts += "'%s|%swato|/' + FOLDER_PATH + '/',\n" % (name.replace(" ", "|"), extra_aux_tags)

        # WATO Alias extra info
        if alias:
            servers[real_name].update({'alias': alias})

        if ipaddress:
            servers[real_name].update({'ipaddress': ipaddress})
            ips += "'%s' : '%s',\n" % (real_name, ipaddress)

    duptag = {}
    for k, v in servers.items():
        for k2, v2 in v.items():
            if k2 in duptag:
                if v2 in duptag[k2]:
                    duptag[k2][v2] += 1
            else:
                duptag[k2] = {v2: 1}

    folder_tags = {folder: {}}
    for k, v in duptag.items():
        for k2, v2 in v.items():
            if v2 > 1 and v2 == len(servers):
                folder_tags[folder].update({k: k2})

    for k, v in servers.items():
        for k2, v2 in folder_tags[folder].items():
            servers[k].pop(k2)

    hosts_mk_file = open(pathlocal + "/" + folder + '/hosts.mk', 'w')
    hosts_mk_file.write('all_hosts += [\n')
    hosts_mk_file.write(all_hosts)
    hosts_mk_file.write(']\n\n')

    if len(ips) > 0:
        hosts_mk_file.write('ipaddresses.update({\n')
        hosts_mk_file.write(ips)
        hosts_mk_file.write('})\n\n')

    hosts_mk_file.write('host_attributes.update(\n')
    hosts_mk_file.write(str(servers))
    hosts_mk_file.write(')\n\n')
    hosts_mk_file.close()

    subfolders = folder.lower().split("/")
    while len(subfolders) > 1:
        subfolder = "/".join(subfolders)
        if not os.path.exists(pathlocal + "/" + subfolder + '/.wato'):
            wato_file = open(pathlocal + "/" + subfolder + '/.wato', 'w')
            wato_file.write("{'title': '%s'}\n" % subfolder.upper().split("/")[-1])
            wato_file.close()
        subfolders.pop()[-1]

    wato_file = open(pathlocal + "/" + folder + '/.wato', 'w')
    wato_file.write("{'attributes': %s, 'num_hosts': %d, 'title': '%s'}\n" %
                    (folder_tags[folder], len(folders[folder]), folder.upper().split("/")[-1]))
    wato_file.close()
