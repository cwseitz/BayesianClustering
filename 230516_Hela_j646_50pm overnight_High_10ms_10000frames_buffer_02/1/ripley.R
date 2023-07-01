library(spatstat)

# Read the CSV file
data <- read.csv("data.txt")

# Create a point pattern object
points <- ppp(data$x, data$y, window = owin(range(data$x), range(data$y)))

# Set the maximum distance for estimation
r_max <- 10  # Set your desired maximum distance

# Compute the L-function
L <- Lest(points,rmax=r_max)

L$bord  <- L$bord  - L$r
# Plot the L-function
plot(L)

# Compute the pair correlation function
pcf_result <- pcf(points)

# Plot the pair correlation function
plot(pcf_result)