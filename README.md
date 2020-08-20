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

Noise lines paper: https://ui.adsabs.harvard.edu/abs/2018PhRvD..97h2002C/abstract
Data release O1 and O2 https://ui.adsabs.harvard.edu/abs/2019arXiv191211716T/abstract
Galactic center search between 10 and 710 Hz https://ui.adsabs.harvard.edu/abs/2020PhRvD.101h2004P/abstract
