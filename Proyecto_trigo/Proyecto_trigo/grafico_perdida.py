import matplotlib.pyplot as plt

decadas = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
perdida = [24.893231, 22.082780, 8.897762, 5.197643, 5.798681, 6.999317, 4.736521]

plt.figure(figsize=(9,5))
plt.bar(decadas, perdida, color='#D4A017')
plt.plot(decadas, perdida, color='black', marker='o', linewidth=2)

plt.title('Evolución del % de pérdida de trigo por década\n1960-2026', fontsize=14, fontweight='bold')
plt.ylabel('% Pérdida promedio ( (Sembrada - Cosechada) / Sembrada )')
plt.xlabel('Década')
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(perdida):
    plt.text(i, v+0.5, f"{v:.1f}%", ha='center', fontweight='bold')

plt.tight_layout()

# Primero lo guarda
plt.savefig('perdida_por_decada.png', dpi=300)

# Después lo muestra en otra ventana
plt.show()