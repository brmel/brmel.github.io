---
title: "How I Fixed an IA Algorithm in Scikit-Learn"
date: 2024-04-29
summary: "K-means in scikit-learn could hang forever. Three conditions had to line up — duplicate points, k equal to the number of points, and a very particular initialisation — and the empty-cluster fix created the empty cluster it was fixing."
description: "Finding and reporting an infinite loop in scikit-learn's K-means empty-cluster handling, and how the fix was reached."
tags: ["Python", "scikit-learn", "Machine Learning", "K-means", "Open Source"]
categories: ["Machine Learning"]
cover:
    image: "01-kmeans-bug-repro.jpg"
    alt: "Scatter plot of the failing case, with input data points and cluster centres marked"
    relative: true
canonicalOriginal: "https://www.linkedin.com/pulse/how-i-fixed-ia-algorithm-scikit-learn-library-brahim-redouane-mellah--ne59e"
canonicalOriginalName: "LinkedIn"
---

As a software developer, one of the things I love doing at work is studying edge
cases and boundaries of algorithms, especially mathematical ones, to define their
limits and constraints.

Recently, I was experimenting with a machine learning algorithm, K-means,
implemented in the
[scikit-learn library](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html),
which is one of the best open-source repositories for mathematical and machine
learning algorithms. During this exploration, I discovered a bug that was causing
the K-means implementation to get stuck in an infinite loop.

In the next section, I will provide a brief explanation of K-means, describe the
bug, and the proposed solution that was implemented in the library.

> **Personal opinion.** I think everyone should help make open source better
> however they can, as long as it doesn't hurt their business. Open source is a
> great idea and has had a big impact on our world. Leaders of big tech companies
> should support it more.

## K-means

The k-means algorithm is a popular unsupervised machine learning technique used
for clustering data. The goal of the k-means algorithm is to partition a set of
data points into *k* clusters where each data point belongs to the cluster with
the nearest mean. The standard algorithm was first proposed by Stuart Lloyd of
[Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs) in 1957.

K-means has two inputs: the number of clusters *k*, and the data points. Some
implementations also support optional initial centroids. These are the main
steps:

1. **Initialization** — choose *k* initial cluster centroids from the data points
   (this could be random or based on some statistics).
2. **Assignment step** — assign each data point to the nearest cluster centroid
   based on a distance metric (typically Euclidean distance). This step creates
   clusters.
3. **Update step** — recalculate the centroids of the clusters based on the
   current assignment of data points. The new centroid is the mean of all data
   points assigned to that cluster.
4. **Repeat** — alternate between the assignment step and the update step until
   the centroids no longer change significantly, or a maximum number of
   iterations is reached, or some other stop condition.

## The bug

I noticed that a weird behaviour happens if we encounter an empty cluster in a
very particular condition. If a cluster becomes empty during the execution of the
k-means algorithm, it typically indicates a scenario where no data points are
assigned to that cluster. This situation can occur due to several reasons, but
mainly poor initialization and data distribution.

In scikit-learn, to solve the problem of empty clusters, they decided to
associate at least one data point to each empty cluster, and they were relocating
data points that are far away from their centroids to do that job.

The idea is good, but there was no check that the algorithm is not generating an
empty cluster when trying to fill an empty cluster. And I noticed that if the
following three conditions are satisfied, the algorithm gets stuck in an infinite
loop:

1. There are duplicate input data points.
2. The number of clusters is equal to the total number of data points.
3. Very specific initial positions.

Here is a minimal example that reproduced the bug:

{{< figure src="01-kmeans-bug-repro.jpg" alt="Scatter plot of the failing case: green input data points, several of them duplicated at the same coordinates, and blue cluster centres" caption="A example that reproduced the bug. Green marks the input data, blue the cluster centres — note the duplicated points sharing coordinates." >}}

## The fix

There are several strategies to address this issue:

- Ensure that the relocation algorithm does not create an empty cluster when
  attempting to fill one.
- In certain cases, it may be beneficial to remove duplicate points.
- Reduce the number of clusters used if the specified number of clusters exceeds
  the number of unique input data points.

You can learn more about the strategy that was finally used by reading the
discussion of the resolved issue:
[scikit-learn#28055](https://github.com/scikit-learn/scikit-learn/issues/28055).

To propose a fix for an open-source algorithm in general, one way is to open an
issue in their GitHub repo. Scikit-learn did a good job documenting how you
should do it:
[scikit-learn contributing](https://scikit-learn.org/stable/developers/contributing.html).
I followed the steps, and I opened an issue that was resolved quickly, in my
opinion.

## The lessons

- Handling edge cases and boundaries of algorithms is crucial and should not be
  ignored, because they can cause real problems in production code.
- Fixing open-source code can be time-consuming, and without sufficient
  motivation, people may not put effort into it.

## Sources

- scikit-learn — [`KMeans` documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- scikit-learn — [issue #28055](https://github.com/scikit-learn/scikit-learn/issues/28055), the bug and its discussion
- scikit-learn — [contributing guide](https://scikit-learn.org/stable/developers/contributing.html)
- Wikipedia — [Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs), where Lloyd proposed the algorithm in 1957
