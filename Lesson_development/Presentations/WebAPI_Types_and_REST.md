
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

## REST API methods

![*Source:* https://www.numpyninja.com/post/rest-api-for-dummies-explained-using-mommies ](assets/img/rest_api.jpg) 

There are five HTTP methods that you can use when making an API request:

- `GET` - retrieve a data from database / server.

- `POST` - create a new record.

- `PUT` - modify / replace the record. It replaces the entire record.

- `PATCH` - modify / update the record. It replaces parts of the record.

- `DELETE` - delete the record.

### Request structure

![*Source:* https://www.altexsoft.com/blog/rest-api-design/ ](assets/img/rest_request.png)

Apart from the HTTP methods, you need a few other components to make the API request. The components are: 

- **HTTP method** - to explain what action you want to perform
- **endpoint** - a URL to find the resource you are trying to reach on the Internet. The endpoint contains of **Base URL** (or root endpoint) - a consistent part of the URL to use and **relative URL** - reference to specific resource you want to access.
- **headers** - provides information relevant both for client (us) and the server.It can be used for example for authentication or to provide information about the body content.See the full list of valid [HTTP headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- **body** - contains data that you want to send to the server. 

:::info
### Passing parameters
- **`GET`** request parameters are usually included in the endpoint URL.  
- **`PUT`** and **`POST`** methods accept parameters in the request body.

### HTTP status codes 

Once you send the request to the server, you will receive a response with a status code. Here are some responses that you might see: 

| **Status Code**           | **Description**             |
|---------------------------|-----------------------------|
| 200 OK                    | Request has succeeded       |
| 201 Created               | Request has succeeded and  a new resource has been  created as a result         |
| 400 Bad Request           | Request could not be understood due to incorrect syntax |
| 403 Forbidden             | Client does not have  access rights to the content|
| 404 Not Found             | Server can not find the  requested resource          |
| 500 Internal server error | Server encountered an unexpected condition that prevented it from fulfilling the request                           |

Any status codes in the 200s mean the request was successful (although this doesn't
necessarily mean it did what you wanted it to do). The 400s mean we did
something wrong. 500s means something is likely wrong on the other end.
We might see `401`, which means we either aren't authorised to access what we
are trying to access, or our authentication step went wrong.
A `404` means the resource we are looking for was not found (just like for websites).

Please see the full list of [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses).

## Authentication 

The 4TU.ResearchData Web API is a public - anyone can access it. 
However, you need to authenticate yourself to be able to perform some of the actions. 
By and large if you need to log in in the web interface to perform an action, 
it means you would need a authentcation token to do the same via web API -
 it's usually in the cases when you're using a method that alters the database). 
Today we will create and use an authentication token using a *personal access token*.

Remember, it's a secret key, that you never want to share with the world.

:::danger
## Important
Never type you token in the script! that you may share, accidentally or otherwise.
:::

A good way to store your personal access token is to include it Set the environment variable on your system or in a `.env` file:

