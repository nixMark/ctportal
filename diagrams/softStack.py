from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.compute import Server
from diagrams.digitalocean.network import Domain
from diagrams.onprem.client import Client
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.logging import Loki
from diagrams.onprem.network import Traefik, Consul

with Diagram("Software Stack", filename="output/software_stack.png",show=False):
    Internet = Domain("*.huntshowdown.com")
    
    Central = Server("Central Data Server")
    Steam = Custom("Steam Auth Servers", "images/steam2.png")
    Player = Client("Player")
    
    with Cluster("MP Server"):
        Cache = Redis("Cache & Transaction\nServer")
        Registry = Consul("Registry")
        CryEngine = Custom("CryEngine MP\nServer", "images/cryengine.png")
        EasyAC = Custom(" ", "images/easy.png")
        Proxy = Traefik("Application Proxy")
 
        with Cluster("Monitoring and Logging"):
            Prometheus = Prometheus("Monitoring Data\nCollector")
            Loki = Loki("Logging Data Collector")
    
    Player    >> Steam
    Player    >> Internet
    Steam     >> Internet
    Internet  >> Proxy
    Proxy     >> EasyAC
    Proxy     >> Registry
    CryEngine >> Cache
    CryEngine >> EasyAC
    Cache     >> Central
    CryEngine >> Central
    
    Cache     >> Edge(color="firebrick", style="dashed") >> Prometheus
    Proxy     >> Edge(color="firebrick", style="dashed") >> Prometheus
    Registry  >> Edge(color="firebrick", style="dashed") >> Prometheus
    CryEngine >> Edge(color="firebrick", style="dashed") >> Prometheus
    
    Cache     >> Edge(color="firebrick", style="dashed") >> Loki
    Proxy     >> Edge(color="firebrick", style="dashed") >> Loki
    Registry  >> Edge(color="firebrick", style="dashed") >> Loki
    CryEngine >> Edge(color="firebrick", style="dashed") >> Loki