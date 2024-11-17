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
