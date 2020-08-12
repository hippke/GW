# GW
Gravitational wave analysis
https://www.uv.es/virgogroup/Denoising_ROF.html

Manuell FFT
https://www.gw-openscience.org/tutorial05/
NFFT = 1024
window = np.blackman(NFFT)
plt.subplot(325)
spec_power, freqs, bins, im = plt.specgram(strain_seg, NFFT=NFFT, Fs=fs, 
                                    window=window)
