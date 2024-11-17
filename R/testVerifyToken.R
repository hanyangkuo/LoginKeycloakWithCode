library(jose)

token <- "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDkxODNkMC0wZWJlLTQyMDEtYWY5MC0yNTMzNmI1ZjEwNTIifQ.eyJleHAiOjE3MzE4NTYxMDMsImlhdCI6MTczMTg1NTk4MywianRpIjoiNGI0NjgzODMtNDcyYS00ZWM2LWJhMTYtNGZiZTYxOWZhZTY5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy90ZXN0Iiwic3ViIjoiODE0MGQ3ZmYtNjFhMC00MzA0LWIyNmItOTViOWRmNTE3YTY4IiwidHlwIjoiU2VyaWFsaXplZC1JRCIsInNpZCI6IjZlMTExMGEzLTBmNTAtNGNhNi1iMTA4LTE1M2FiZDBhZTRmYyIsInN0YXRlX2NoZWNrZXIiOiJFYmN3bzA4bmptZHpITFRpLVlGblprUzdCNTMtR0JIOG02RzdkVGxrZ0I4In0.bO5Cxrs4R8UphWDahEPcu1WUJ8elNYjbHVwTGbPRuOL1XwcqgTCz6g7-KKqXqPivLlCoio6yyIjqgQTnV08CFw"

decoded <- jwt_split (token)
exp_time <- decoded$payload$exp
current_time <- as.numeric(Sys.time())
# Check if the token is expired
if (!is.null(exp_time) && exp_time > current_time) {
  print(TRUE) # Token is valid
} else {
  print(FALSE) # Token is expired
}
