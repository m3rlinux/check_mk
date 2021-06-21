$datafile = "D:\inetpub\wwwroot\nagios.txt"
$allarmi = import-csv $datafile -header descr, status, other -delimiter ";" | where-object {$_.status -eq 1}
$sonde = $allarmi | Select -ExpandProperty "descr"
$sondeOneLine = $sonde -join ", "
if ($sondeOneLine){
	Write-Host "2 Check_Globale_Infrastrutture - Sonde in allarme: $sondeOneLine"
}else{
	Write-Host "0 Check_Globale_Infrastrutture - Non ci sono sonde in allarme"
}