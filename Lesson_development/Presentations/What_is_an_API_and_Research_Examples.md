
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

