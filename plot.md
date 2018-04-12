Plot
================

Plot
----

``` r
DF <- read.csv("E:/BigData/R2_Example/example_studentlist.csv") 
attach(DF)
plot(age)
```

![](plot_files/figure-markdown_github/unnamed-chunk-2-1.png)

``` r
par(mfrow=c(2,2))
plot(height, weight)
plot(weight~height)
plot(height,sex)
plot(height~sex)
```

![](plot_files/figure-markdown_github/unnamed-chunk-2-2.png)

``` r
plot(DF[,c(3,7,8)])
```

![](plot_files/figure-markdown_github/unnamed-chunk-2-3.png)

``` r
par(mfrow=c(1,2))
plot(weight~height)
hMean <- mean(height)
wMean <- mean(weight)
plot(weight~height, pch=as.integer(sex), ann=FALSE)
legend("topleft", c("man", "woman"), pch=sex)
title(main="correlaton between A and B")
title(xlab = "height", ylab="weight")
grid()
abline(v=hMean, h= wMean, col=c("red","orange"))
```

![](plot_files/figure-markdown_github/unnamed-chunk-3-1.png)

``` r
coplot(weight~height | sex)
```

![](plot_files/figure-markdown_github/unnamed-chunk-4-1.png)

``` r
tblBlood <- table(DF$bloodtype)
barplot(tblBlood)
title(main = "bar plot of Blood", ylab = "count")
```

![](plot_files/figure-markdown_github/unnamed-chunk-5-1.png)

``` r
bhei <- tapply(height, bloodtype, mean)
par(mfrow=c(2,2))
barplot(bhei, ylim = c(0,200))
boxplot(height~bloodtype)
hist(height, breaks = 2, prob = T)
lines(density(height))
points(height)
BPoint = seq(min(height), max(height) +5, by= 5)
hist(height, breaks = BPoint)
```

![](plot_files/figure-markdown_github/unnamed-chunk-6-1.png)

``` r
par(mfrow=c(2,3))
plot(height, weight)
boxplot(sex, weight)     
hist(table(bloodtype))     
boxplot(height)
boxplot(height ~ bloodtype)
hist(height, prob=T, breaks = BPoint)
```

![](plot_files/figure-markdown_github/unnamed-chunk-7-1.png)

ggplot2
-------

``` r
library(ggplot2)
library(ggthemes)

ggplot(data = diamonds, aes(carat, price, colour = clarity)) +
  geom_point() +
  theme_wsj()
```

![](plot_files/figure-markdown_github/unnamed-chunk-8-1.png)

``` r
g1 <- ggplot(data = diamonds, aes(carat, price, colour = clarity))
g2 <- geom_line(alpha=0.5)
g3 <- theme_wsj()

g1 <- ggplot(data = DF, aes(height, weight, colour = bloodtype))
g1 + g2 + g3 + geom_point(size=3, alpha=0.8)
```

![](plot_files/figure-markdown_github/unnamed-chunk-9-1.png)

``` r
g4 <- facet_grid(.~sex)
g1 + g2 + geom_point() + g3 + g4
```

![](plot_files/figure-markdown_github/unnamed-chunk-10-1.png)
