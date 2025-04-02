
# 🌐 Types of Web APIs and Why REST is Most Used

## 🔍 Overview of Web API Types

| Type     | Protocol        | Format        | Best For                        | Example Use Cases                           |
|----------|------------------|---------------|----------------------------------|---------------------------------------------|
| REST     | HTTP/HTTPS       | JSON, XML     | Public APIs, data sharing        | 4TU.ResearchData, GitHub, Twitter           |
| SOAP     | SOAP over HTTP   | XML           | Enterprise systems, high security| Banking, healthcare systems                 |
| GraphQL  | HTTP/HTTPS       | JSON          | Custom queries, efficiency       | Facebook API, GitHub GraphQL                |
| gRPC     | HTTP/2           | Protobuf      | High performance, microservices  | Google internal APIs, Kubernetes            |

---

## ✅ Why is REST the Most Used Web API?

| Reason             | Explanation                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Simplicity**      | Easy to use with standard tools like `curl` or `requests` in Python        |
| **Uses HTTP**       | Works with the same protocol as the web                                    |
| **Stateless**       | Each request is independent; better for scalability                        |
| **Human-readable**  | Typically uses JSON — easy to debug and understand                         |
| **Language-agnostic**| Works with all major programming languages                                |
| **Community support**| Huge ecosystem and documentation                                          |

---

## 🎓 Why REST is Ideal for Research

- Works great with tools like Python, R, Jupyter, and shell scripts.
- Data repositories (e.g., **4TU.ResearchData**, **Zenodo**, **Figshare**) use REST APIs.
- Simplifies **data publication, access, and automation** in the research lifecycle.
- Reduces manual work and encourages reproducibility.

---

## 📚 Examples in Practice

- Use `GET` to retrieve datasets programmatically.
- Use `POST` to publish new datasets from your script.
- Use `PUT` or `PATCH` to update metadata.

