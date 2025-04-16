
# 🌐 Introduction to Web APIs and REST

## 🔍 Types of Web APIs

| Type     | Protocol        | Format        | Best For                        | Example Use Cases                           |
|----------|------------------|---------------|----------------------------------|---------------------------------------------|
| **REST**     | HTTP/HTTPS       | JSON, XML     | Public APIs, data sharing        | 4TU.ResearchData, GitHub, Twitter           |
| **SOAP**     | SOAP over HTTP   | XML           | Enterprise systems, high security| Banking, healthcare systems                 |
| **GraphQL**  | HTTP/HTTPS       | JSON          | Custom queries, efficiency       | Facebook API, GitHub GraphQL                |
| **gRPC**     | HTTP/2           | Protobuf      | High performance, microservices  | Google internal APIs, Kubernetes            |

---

## ✅ Why REST is the most popular Web API style

| Reason             | Explanation                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Simplicity**      | Easy to use with standard tools like `curl` or `requests` in Python        |
| **Uses HTTP**       | Works with the same protocol as the web                                    |
| **Stateless**       | Each request is independent; better for scalability                        |
| **Human-readable**  | Typically uses JSON — easy to debug and understand                         |
| **Language-agnostic**| Works with all major programming languages                                |
| **Community support**| Huge ecosystem and documentation                                          |

---

## 🎓 Why REST is great for research

- Works great with tools like Python, R, Jupyter, and shell scripts.
- Data repositories (e.g., **4TU.ResearchData**, **Zenodo**, **Figshare**) use REST APIs.
- Simplifies **data publication, access, and automation** in the research lifecycle.
- Reduces manual work and encourages reproducibility.

---

## Understanding REST API methods

![](https://codimd-cdn.rs.tudelft.nl/codimd/uploads/upload_a32f8824102b6764190f61111043287d.jpg)
*Source:* https://www.numpyninja.com/post/rest-api-for-dummies-explained-using-mommies 

There are five HTTP methods that you can use when making an API request:

| Method   | Description                                              |
|----------|----------------------------------------------------------|
| `GET`    | Retrieve data from the database/server.                  |
| `POST`   | Create a new record.                                     |
| `PUT`    | Modify/replace the record. Replaces the entire record.   |
| `PATCH`  | Modify/update the record. Replaces parts of the record.  |
| `DELETE` | Delete the record.                                       |


### Anatomy of REST API request

![](https://codimd-cdn.rs.tudelft.nl/codimd/uploads/upload_a4993cefd3afd34f2b67044b3c3d2e64.png)
*Source:* https://www.altexsoft.com/blog/rest-api-design/ 

Apart from the HTTP methods, you need a few other components to make the API request. The components are: 

| Component     | Description                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HTTP method** | Specifies the action you want to perform (e.g., `GET`, `POST`, `PUT`, `DELETE`).                                                                                                                                                                                                             |
| **Endpoint**    | A URL to locate the resource on the Internet. Consists of:<br>• **Base URL** – the consistent part of the URL.<br>• **Relative URL** – the specific reference to the resource.                                                                                                               |
| **Headers**     | Provide information relevant to both the client and server. Often used for authentication or describing body content. [See full list of HTTP headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields).                                                                           |
| **Body**        | Contains data you want to send to the server (mainly used in `POST`, `PUT`, or `PATCH` requests).                                                                                                                                                                                           |


:::info
#### Passing parameters
- **`GET`** request parameters are usually included in the endpoint URL.  
- **`PUT`** and **`POST`** methods accept parameters in the request body.
:::

### Common Status Codes & Errors 

Once you send the request to the server, you will receive a response with a status code. Here are some responses that you might see: 

#### ✅ 2xx Success

| **Status Code**     | **Description**                                        |
|---------------------|--------------------------------------------------------|
| **200 OK**          | ✅ The request has succeeded.                          |
| **201 Created**     | ✅ A new resource has been successfully created.       |

#### ⚠️ 4xx Client Errors

| **Status Code**     | **Description**                                                   |
|---------------------|-------------------------------------------------------------------|
| **400 Bad Request** | ⚠️ The server couldn't understand the request due to bad syntax.  |
| **401 Unauthorized**| ⚠️ Authentication is required or has failed.                      |
| **403 Forbidden**   | ❌ The client does not have access rights to the content.          |
| **404 Not Found**   | ❌ The server cannot find the requested resource.                  |

#### 💥 5xx Server Errors

| **Status Code**               | **Description**                                                                 |
|-------------------------------|---------------------------------------------------------------------------------|
| **500 Internal Server Error** | 💥 The server encountered an unexpected condition.                              |

:::info
#### TIP
- **2xx** codes mean success (although this doesn't  mean it did what you wanted it to do)
- **4xx** errors are usually your fault (e.g., bad syntax, unauthorized access). 
- **5xx** errors mean something went wrong on the server.
:::

See the full list of [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses).



### Authentication in REST APIs

The 4TU.ResearchData Web API is public—anyone can access it for basic data retrieval.
However, to perform certain actions (like uploading, editing, or deleting data), you need to authenticate yourself.

As a general rule:

>If you need to log in via the web interface to perform an action, you’ll also need an authentication token to do the same through the API.
This is typically required when using methods that alter the database (e.g., POST, PUT, DELETE).

In this workshop, we'll create and use a personal access token to authenticate our requests.

Remember, it's a secret key, that you never want to share with the world!

:::danger 
#### ⚠️  Important ⚠️ 
Never hard-code your token into scripts — especially if you plan to share them, even accidentally.
:::

A better and safer way to store your token is by using an environment variable on your system. 

You can  or place it in a `.env` file  and store it in the root of the project. This file should never be shared or committed to version control. 

Example of an `.env` file:

```shell=
API_TOKEN=your-secret-token-goes-here
```
To make sure you never accidentally upload your token to GitHub or another repository, add this to your `.gitignore`:

```shell=
.env
```
