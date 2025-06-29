from abc import ABC, abstractmethod
import requests


# -------------------------------------------------------------------------------------------
# Interface (Subject)
class ISubject(ABC):
    @abstractmethod
    def request(self):
        pass

# Real Subject
class RealSubject(ISubject):
    def request(self):
        print("RealSubject: Handling heavy request (e.g., loading 4K video)")

# -------------------------------------------------------------------------------------------
# Virtual Proxy (Lazy Loading)
class VirtualProxy(ISubject):
    def __init__(self):
        self._real_subject = None  # Lazy initialization

    def request(self):
        if self._real_subject is None:
            print("VirtualProxy: Creating RealSubject (only when needed)")
            self._real_subject = RealSubject()
        self._real_subject.request()


# -------------------------------------------------------------------------------------------
# Protection Proxy (Access Control)
class ProtectionProxy(ISubject):
    def __init__(self, user):
        self._real_subject = RealSubject()
        self._user = user

    def request(self):
        if self._user == "admin":
            print("ProtectionProxy: Access granted for admin")
            self._real_subject.request()
        else:
            print("ProtectionProxy: Access denied for non-admin users")


# -------------------------------------------------------------------------------------------
# Remote Proxy (Network Simplification)
class RemoteProxy(ISubject):
    def __init__(self, api_url):
        self._api_url = api_url

    def request(self):
        print(f"RemoteProxy: Forwarding request to {self._api_url}")
        response = requests.get(self._api_url)
        print(f"Remote response: {response.text[:140]}...")



# -------------------------------------------------------------------------------------------
# client code
def client_code(subject: ISubject):
    print("Client: Starting interaction with subject")
    subject.request()
    print()


# Usage
if __name__ == "__main__":
    print("=== Virtual Proxy ===")
    client_code(VirtualProxy())

    print("\n=== Protection Proxy ===")
    client_code(ProtectionProxy("admin"))
    print("=== Protection Proxy denial ===")
    client_code(ProtectionProxy("guest"))  # Try "guest" to see denial

    print("\n=== Remote Proxy ===")
    client_code(RemoteProxy("https://api.github.com"))
