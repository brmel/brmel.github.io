---
title: "How an Image-Processing Feature Saved My Flight: Barcodes and Foreground Colour"
date: 2025-12-03
tags: ["Image Processing"]
summary: "A real-world example of why foreground color support in barcode reading matters."
cover:
    image: "01-boarding-pass-dark.jpeg"
    alt: "Barcode in Dark Mode"
    relative: true
---

One day I was in Düsseldorf airport to take a flight. I had already checked-in online and only had the barcode on my phone.

{{< figure src="01-boarding-pass-dark.jpeg" alt="Barcode in Dark Mode" width="200" >}}

When I arrived at the security checkpoint to scan my barcode, it didn’t work. I was already late. I tried every zoom, rotation… nothing.
The security guy told me I needed to go back to the check-in gate and hope they were still there to print a paper boarding pass.

But then I realized: my phone was in dark mode, and the barcode was shown with dark as foreground color. So I just switched to light mode… and it saved me time, my flight, and a lot of stress.

{{< figure src="02-boarding-pass-read.jpeg" alt="Barcode in Light Mode" width="200" >}}

A reader that assumes dark-on-light is a reader that works everywhere except on
a phone at night, which is where boarding passes actually live. Foreground
colour is a setting in every serious imaging library — including the
[Aurora Imaging Library](https://www.zebra.com/us/en/software/machine-vision-and-fixed-industrial-scanning-software/aurora-imaging-library.html)
I work on — and it costs nothing to set it correctly.

I still switch to light mode before every gate.
