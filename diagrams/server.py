from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server
from diagrams.digitalocean.network import Domain

# lattitude.sh - SA
# Leaseweb - Rest of the world

with Diagram("Server infrastructure",filename="output/servers.png", show=False, direction="TB"):


    with Cluster("Americas"):
        with Cluster("US"):    
            with Cluster("US - East"):
                cs1_wc = Server("cs1-lv-lw-wc.\nhuntshowdown.com") 
                cs2_wc = Server("cs2-lv-lw-wc.\nhuntshowdown.com") 
            with Cluster("US - West"):
                cs1_sj = Server("cs1-lv-lw-sj.\nhuntshowdown.com") 
                cs2_sj = Server("cs2-lv-lw-sj.\nhuntshowdown.com") 
        with Cluster("South America"):
            # SAO
            # SAO2
            cs1_br = Server("cs1-lv-mxh-br.\nhuntshowdown.com") 
            cs2_br = Server("cs2-lv-mxh-br.\nhuntshowdown.com") 
    with Cluster("APAC"):        
        with Cluster("Asia"):
            # Hong Kong HKG-10 Data Center
            # Hong Kong HKG-12 Data Center
            cs2_hk = Server("cs2-lv-lw-hk.\nhuntshowdown.com") 
            cs3_hk = Server("cs3-lv-lw-hk.\nhuntshowdown.com") 
        with Cluster("Oceania"):
            # Sydney SYD-10 Data Centre
            # Sydney SYD-11 Data Center
            # Sydney SYD-12 Data Center
            cs3_au = Server("cs3-lv-lw-au.\nhuntshowdown.com") 
            cs4_au = Server("cs4-lv-lw-au.\nhuntshowdown.com")
    with Cluster("EMEA"):
        with Cluster("Russia"):
            cs5_eu = Server("cs5-lv-lw-eu.\nhuntshowdown.com") 
            cs6_eu = Server("cs6-lv-lw-eu.\nhuntshowdown.com") 
        with Cluster("EU"):
            cs1_eu = Server("cs1-lv-lw-eu.\nhuntshowdown.com") 
            cs2_eu = Server("cs2-lv-lw-eu.\nhuntshowdown.com") 

    capi1_asia = Domain("capi1-lv-asia")
    capi2_asia = Domain("capi2-lv-asia")
    capi1_russian = Domain("capi1-lv-russian")
    capi2_russian = Domain("capi2-lv-russian")
    capi1_oceania = Domain("capi1-lv-oceania")
    capi2_oceania = Domain("capi2-lv-oceania")
    capi1_southamerica = Domain("capi1-lv-southamerica")
    capi2_southamerica = Domain("capi2-lv-southamerica")
    capi1_eu = Domain("capi1-lv-eu")
    capi2_eu = Domain("capi2-lv-eu")
    capi1_useast = Domain("capi1-lv-useast")
    capi2_useast = Domain("capi2-lv-useast")
    capi1_uswest = Domain("capi1-lv-uswest")
    capi2_uswest = Domain("capi2-lv-uswest")

    capi1_asia >> cs2_hk
    capi2_asia >> cs3_hk
    capi1_russian >> cs5_eu
    capi2_russian >> cs6_eu
    capi1_oceania >> cs3_au
    capi2_oceania >> cs4_au
    capi1_southamerica >> cs1_br
    capi2_southamerica >> cs2_br
    capi1_eu >> cs1_eu
    capi2_eu >> cs2_eu
    capi1_useast >> cs1_wc
    capi2_useast >> cs2_wc
    capi1_uswest >> cs1_sj
    capi2_uswest >> cs2_sj