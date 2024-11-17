https://github.com/r-lib/jose/blob/main/man/jwt_encode.Rd

https://jsonplaceholder.typicode.com/posts



```R
library(httr)
library(jsonlite)
library(jwt)

Postman <- setRefClass(
  "Postman",
  fields = list(name = "character", age = "character"),
  
  methods = list(
    initialize = function(name, age) {
      name <<- name
      age <<- age
    },
    
    getResponse = function() {
      url <- "https://jsonplaceholder.typicode.com/todos/1"
      headers <- add_headers(
        Authorization = "Bearer YOUR_ACCESS_TOKEN",
        Accept = "application/json"
      )
      
      response <- GET(url, headers)
      content <- content(response, "text")
      return(content)
    },
    
    writeResponse = function(text) {
      basepath <- file.path(Sys.getenv("LOCALAPPDATA"), "testproject")
      filepath <- file.path(basepath, "token")
      cat("Filepath:", filepath, "\n")
      
      if (!dir.exists(basepath)) {
        dir.create(basepath, recursive = TRUE)
      }
      
      write(text, filepath)
    },
    
    readResponse = function() {
      basepath <- file.path(Sys.getenv("LOCALAPPDATA"), "testproject")
      filepath <- file.path(basepath, "token")
      cat("Filepath:", filepath, "\n")
      
      if (file.exists(filepath)) {
        return(readLines(filepath))
      } else {
        return(NULL)
      }
    }
  )
)

verifyToken <- function(token) {
  tryCatch(
    {
      decoded <- jwt_decode_hmac(token, secret = NULL, verify = FALSE)
      return(TRUE)
    },
    error = function(e) {
      return(FALSE)
    }
  )
}

# Main execution
postman <- Postman$new(name = "Young", age = "18")
print(postman$getResponse())

```


https://chatgpt.com/share/673a093d-b2d8-8002-bee5-01706aed6958

