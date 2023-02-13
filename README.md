Azure Architecture
This architecture consists of a Hub and Spoke VNet configuration with VNet peering between them. The Hub VNet contains a private DNS zone, an Azure Container Registry, a Key Vault, and an Azure SQL Database. There are three spoke vnets in the architecture:

Spoke 1 VNet contains an Azure Container Registry with private endpoints enabled and an API Management Service without private endpoints.
Spoke 2 VNet contains an Azure Web App with private endpoints and a Key Vault with private endpoints. The Azure Web App is able to communicate with the Azure Container Registry via the Hub VNet privately and is able to deploy containers.
Spoke 3 VNet contains an Azure SQL Database with private endpoints, and the Azure Web App is able to communicate with the database privately via the Hub VNet.
No spoke can communicate with each other directly, the communication path must go through the Hub VNet. All the private DNS zones of each resource type are present in the Hub VNet, so the private endpoints of the various spokes should be able to resolve the FQDNs of the resource type.

Architecture Diagram
The following Mermaid diagram describes the architecture:

``` mermaid
graph LR
    subgraph Hub Vnet
        Hub_Vnet[Hub Vnet]
        Private_DNS_Zone[Private DNS Zone]
        Azure_Container_Registry[Azure Container Registry]
        Key_Vault[Key Vault]
        SQL_Database[SQL Database]
    end
    
    subgraph Spoke 1 Vnet
        Spoke_1_Vnet[Spoke 1 Vnet]
        Azure_Container_Registry_PE[Azure Container Registry<br>with Private Endpoints]
        API_Management_Service[API Management Service]
    end
    
    subgraph Spoke 2 Vnet
        Spoke_2_Vnet[Spoke 2 Vnet]
        Azure_Web_App_PE[Azure Web App<br>with Private Endpoints]
        Key_Vault_PE[Key Vault<br>with Private Endpoints]
    end
    
    subgraph Spoke 3 Vnet
        Spoke_3_Vnet[Spoke 3 Vnet]
        Azure_SQL_Database_PE[Azure SQL Database<br>with Private Endpoints]
    end
    
    Hub_Vnet -- Private_DNS_Zone
    Hub_Vnet -- Azure_Container_Registry
    Hub_Vnet -- Key_Vault
    Hub_Vnet -- SQL_Database
    
    Spoke_1_Vnet -- Azure_Container_Registry_PE
    Spoke_1_Vnet -- API_Management_Service
    
    Spoke_2_Vnet -- Azure_Web_App_PE
    Spoke_2_Vnet -- Key_Vault_PE
    
    Spoke_3_Vnet -- Azure_SQL_Database_PE
    
    Azure_Web_App_PE -- Azure_Container_Registry_PE[Deploy and manage containers]
    Azure_Web_App_PE -- Key_Vault_PE[Store and retrieve secrets]
    Azure_Web_App_PE -- Azure_SQL_Database_PE[Access database]
    
    Private_DNS_Zone -- Azure_Web_App_PE[Resolve FQDNs]
    Private_DNS_Zone -- Azure_Container_Registry
```
