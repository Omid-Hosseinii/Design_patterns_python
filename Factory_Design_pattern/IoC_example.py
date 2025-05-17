from dependency_injector import containers, providers


class ApiClient:
    def fetch(self):
        return "data from API"

class ReportService:
    def __init__(self, client: ApiClient):
        self.client = client
    def generate(self):
        print("Report:", self.client.fetch())



class Container(containers.DeclarativeContainer):
    config  = providers.Configuration()               # optional settings node

    api_client     = providers.Singleton(ApiClient)   # build once, reuse
    report_service = providers.Factory(
        ReportService,
        client=api_client,                            # wire dependency
    )


container = Container()
service = container.report_service()  # Factory builds fresh object each call
service.generate()





