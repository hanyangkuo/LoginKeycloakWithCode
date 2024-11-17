library(R6)
library(httr)
library(jsonlite)

test <- R6Class("Test",
  private = list(
    a = NULL,
    b = NULL,
    
    add = function(){
      return(private$a + private$b)
    }
  ),
  
  public = list(
    # Initialize function to set a and b
    initialize  = function(a, b) {
      private$a <- a
      private$b <- b
    },
    printSum = function(){
      sum_result <- private$add()
      print(sum_result)
    }
  )
)

test_instance <- test$new(a = 10, b = 20)

test_instance$printSum()



res = httr::GET("https://jsonplaceholder.typicode.com/todos/1")
print(res)


