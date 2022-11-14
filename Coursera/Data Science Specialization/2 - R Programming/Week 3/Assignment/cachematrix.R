## Following function transform a matrix in a list of 4 functions enabling
## to get access to/modify the matrix and its inverse

makeCacheMatrix <- function(x = matrix()) {
  m <- NULL
  set <- function(y) {
    x <<- y
    m <<- NULL
  }
  get <- function() x
  setinverse <- function(solve) m <<- solve
  getinverse <- function() m
  list(set = set, get = get,
       setinverse = setinverse,
       getinverse = getinverse)
}


## Follofwing function stores in a cache the inverse of a matrix
## if the inverse of the matrix has already been calculated, get it from the cache

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
  m <- x$getinverse()
  if(!is.null(m)) {
    message("getting cached data")
    return(m)
  }
  data <- x$get()
  m <- solve(data, ...)
  x$setinverse(m)
  m
}

#test on a matrix
my_matrix <- matrix(c(-3,-1,1,5,2,-1,6,2,-1),3,3)

my_matrix2 <- makeCacheMatrix(my_matrix)

my_matrix2$getinverse()

cacheSolve(my_matrix2)
cacheSolve(my_matrix2)

my_matrix2$getinverse()
