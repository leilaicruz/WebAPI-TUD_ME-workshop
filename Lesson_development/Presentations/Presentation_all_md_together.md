
# 🔧 Workshop: Data access & Publication with the 4TU.ResearchData WEBAPI

**Duration**: 90 minutes  
**Audience**: Researchers in mechanical engineering & research data support  
**Tools**: [4TU.ResearchData WEB API documentation](https://djehuty.4tu.nl/#titlepage), Unix shell terminal/Git bash for Windows/ WSL for Windows, Python

---

## ✅ Learning Objectives

By the end of the workshop, participants will be able to:

1. **Explain what a REST WEB API is** and how it facilitates access and publication of research data.
2. **Use the 4TU.ResearchData API** to fetch datasets and metadata using curl commands , to search for datasets , to upload datasets 


---

## 🗂️ Workshop Schedule

| Time       | Activity                                                                 |
|------------|--------------------------------------------------------------------------|
| 0–10 min  | **Intro to REST APIs**: Concepts and mechanics                          |
| 10–25 min | **Use case**: Why APIs matter for data reuse & automation              |
| 25–45 min | **Fetching datasets via API (reuse)**  
_Hands-on with curl commands_           |
| 45–60 min | **Uploading datasets via API (publishing)**  
_Hands-on with curl commands_ |          |
| 75–90 min | **Showcase the interaction with the webapi with Python**             |

---


# 🔧 What is an API?

## 📘 Definition
An **API (Application Programming Interface)** is a set of **rules and tools** that allow software applications to communicate with each other.

- Think of it as a **contract** between two software components.
- It defines **how to request services** and **what response to expect**.

---

## 🧠 How APIs Work

APIs expose certain **functions or data** to external users (or internal systems), allowing them to:
- Retrieve information
- Send or modify data
- Trigger actions or computations

APIs can be:
- **Local** (between software on the same machine)
- **Remote** (between software across the internet — aka Web APIs)

---

## 🧪 Examples of APIs in Research

| Use Case                              | Description                                                              | API Type      |
|---------------------------------------|--------------------------------------------------------------------------|---------------|
| Dataset access from repositories      | Query and download datasets from 4TU.ResearchData, Zenodo, Dataverse     | Web API (REST)|
| Publication automation                | Submit and update research outputs programmatically                      | Web API (REST)|
| Metadata enrichment                   | Add ORCID info, grant metadata from Crossref or Fundref                 | Web API (REST)|
| Data analysis environments            | Use APIs in R/Python to call scientific packages (e.g., NumPy, SciPy)   | Local API     |
| Instrument control in laboratories    | Programmatically access sensors and machines (via vendor SDKs/APIs)     | Local API     |
| High-performance computing (HPC) jobs | Submit/monitor jobs using APIs like SLURM or workload managers           | Local/Web API |
| Linked data queries                   | Use SPARQL APIs to extract structured data from semantic repositories    | Web API (SPARQL)|

---

## 🎓 Why Are APIs Important in Research?

- **Automation**: Eliminate repetitive tasks (e.g., uploading new data versions)
- **Reproducibility**: Workflows become scriptable and shareable
- **Scalability**: Analyze or query large datasets remotely without downloading everything
- **Interoperability**: Connect systems like ELNs, data repositories, and lab instruments

---

## 📎 Bonus Tip

Using APIs in your research lets you **build FAIR-aligned workflows**, especially when integrated with metadata standards and versioning tools.







# 🔄 API vs Web API: What's the difference?

## 🧩 Application Programming Interface (API)
- Interface that allows **two software components** to talk to each other.
- Can be **local or remote**, not limited to the web.
- Examples:
  - Python libraries (e.g., `os`, `math`)
  - Operating system APIs
  - Internal research data pipelines

---

## 🌐 Web API (Web-based API)
- **A type of API** that uses **HTTP/S** to communicate over the **internet**.
- Often follows **REST** or **GraphQL** conventions.
- Enables **remote access to data and services**.

---

## 📊 Analogy

| Feature       | API                        | Web API                                      |
|---------------|----------------------------|----------------------------------------------|
| Scope         | Any software interaction   | Interaction via the web                      |
| Protocol      | Various (not just HTTP)    | HTTP/HTTPS                                   |
| Location      | Local or remote            | Remote (web servers)                         |
| Examples      | Python's `os` module       | GitHub API, 4TU.ResearchData API             |
| Research Use  | Internal tools/scripts     | Publishing data, querying datasets remotely  |

---

## 🎓 Research Relevance

- APIs help **structure and automate** research workflows.
- Web APIs enable **integration, publication, and reuse** of research data.



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

