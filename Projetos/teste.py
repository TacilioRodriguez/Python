    {     

    Write-Output "Connecting on $(Get-Date)"



    #######################################################################

    # If you are using an Automation Account, uncomment the following lines 

    #######################################################################

    

    #Connect to Azure using the Run As Account

    Try{

        $servicePrincipalConnection=Get-AutomationConnection -Name "AzureRunAsConnection"

        Connect-AzAccount  -ServicePrincipal -TenantId $servicePrincipalConnection.TenantId -ApplicationId $servicePrincipalConnection.ApplicationId -CertificateThumbprint $servicePrincipalConnection.CertificateThumbprint 

    }

    Catch {

        if (!$servicePrincipalConnection){

            $ErrorMessage = "Connection $connectionName not found."

            throw $ErrorMessage

        } else{

            Write-Output -Message $_.Exception

            throw $_.Exception

        }

    }

    

    #######################################################################

    # Finish Azure Automation Account Section

    #######################################################################



Try{
    Set-AzSqlDatabase -ResourceGroupName $ResourceGroupName -DatabaseName $DatabaseName -ServerName $ServerName -RequestedServiceObjectiveName $RequestedServiceObjectiveName
}

    Catch {

            Write-Output -Message $_.Exception

            throw $_.Exception

        }
}


{

    # Exit

    Write-Output "Finished process on $(Get-Date)"

}