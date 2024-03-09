import numpy as np
import matplotlib.pyplot as plt

def triangle_wave(x, N):
    result = 0.0
    terms = []  
    for n in range(1, N + 1):
        term = (-1)**(n - 1) * (1 / (2 * n - 1)**2) * np.sin((2 * (2 * n - 1) * np.pi * x) / T)
        terms.append(term)
        result += term

    return (8 / np.pi**2) * result, terms

T = 2 * np.pi  
N = 100 

x_values = np.linspace(0, 4 * np.pi, 1000)


y_values_triangle, individual_terms = triangle_wave(x_values, N)

# Her bir Fourier terimini ayrı ayrı çiz
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
for i, term in enumerate(individual_terms, start=1):
    plt.plot(x_values, term, label=f'Terim {i}')

plt.title('Her Bir Fourier Terimi')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Terimlerin toplamını çiz
plt.subplot(2, 1, 2)
plt.plot(x_values, y_values_triangle, label=f'Toplam (N={N}) - Üçgen Dalga')
plt.title('Fourier Serisinin Toplamı')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
