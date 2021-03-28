---
title: Wavetable Synthesis
created: '2021-03-27T17:19:47.165Z'
modified: '2021-03-27T17:26:33.449Z'
---

# Wavetable Synthesis

Generate multiple reference waveforms, with progressively fewer harmonics are we "go up" in frequency.

Note that we may still use higher resolution as we go up.

For example, say the reference fundamental frequency is 2000Hz.

At 44.1KHz:
$$
\frac{1}{2,000} * 44,100=22.05\ samples
$$
For Nyquist, representing the fundamental frequency ($f_0$) will require ~44 samples.

However, we wouldn't have any "space" to do higher harmonics.

If we instead oversample by some amount, say 8x, then we can safely represent up to 8x the $f_0$.

That's the idea behind keeping the ref waveform size $2,048$ samples, even as we scale up in frequency. At higher frequencies, we automatically oversample by a higher factor.

However, we put less higher frequency information as we go up, again because we don't want to alias by shifting $f_1$, $f_2$, ... past the Nyquist frequency.
