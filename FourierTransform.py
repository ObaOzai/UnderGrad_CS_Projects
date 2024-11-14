"""

Fourier Transform Overview
Fourier Transform is a mathematical technique that transforms a time-domain signal into its constituent frequencies.
It's widely used in signal processing, image processing, data compression, audio analysis, and more.

The Discrete Fourier Transform (DFT) is the digital version, and it converts a finite sequence of equally 
spaced samples of a function into a sequence of complex numbers representing frequency components.

The Fast Fourier Transform (FFT) is an efficient algorithm to compute the DFT, significantly reducing the computation time.

Explanation of the Code
Generating a Signal:
We generate a time-domain signal composed of two sine waves with frequencies of 5 Hz and 50 Hz.
Performing FFT:
We use np.fft.fft to compute the Fast Fourier Transform.
We use np.fft.fftfreq to get the corresponding frequencies.
We take only the positive frequencies since the FFT result is symmetric.
Plotting the Results:
The first plot shows the original signal in the time domain.
The second plot shows the magnitude of the FFT, revealing the frequencies present in the signal.

Output
A plot of the original signal showing two combined sine waves.
A frequency spectrum plot showing peaks at 5 Hz and 50 Hz, corresponding to the frequencies present in the original signal.

Try modifying the frequencies (frequency1 and frequency2) and observe how the FFT output changes.
Experiment with adding noise to the signal and see how it affects the frequency spectrum.
Use real-world signals (e.g., audio recordings) to analyze their frequency content.

"""

# Fast Fourier Transform (FFT) Example
# Astro Pema Software (c)
# Oba Ozai & ChatGPT4 Nov 2024

import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
def generate_signal(frequency1=5, frequency2=50, sampling_rate=500, duration=2):
    """
    Generate a sample signal with two frequencies.
    """
    t = np.linspace(0, duration, sampling_rate * duration, endpoint=False)
    signal = np.sin(2 * np.pi * frequency1 * t) + 0.5 * np.sin(2 * np.pi * frequency2 * t)
    return t, signal

# Perform FFT
def perform_fft(signal, sampling_rate):
    """
    Perform Fast Fourier Transform on a signal.
    """
    N = len(signal)
    fft_values = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(N, 1 / sampling_rate)
    
    # Return positive frequencies only
    return fft_freqs[:N // 2], np.abs(fft_values)[:N // 2]

if __name__ == "__main__":
    # Generate a sample signal
    sampling_rate = 500  # 500 samples per second
    t, signal = generate_signal(frequency1=5, frequency2=50, sampling_rate=sampling_rate)
    
    # Perform FFT
    fft_freqs, fft_magnitudes = perform_fft(signal, sampling_rate)
    
    # Plot the original signal
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.title('Time Domain Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
    # Plot the FFT result
    plt.subplot(2, 1, 2)
    plt.stem(fft_freqs, fft_magnitudes, use_line_collection=True)
    plt.title('Frequency Domain (FFT)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# EOF
