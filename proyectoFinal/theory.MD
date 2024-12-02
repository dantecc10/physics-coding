# Reporte del Proyecto Final: Simulación Navier-Stokes

## Conceptos Físicos
### Dinámica de Fluidos
- **Ecuaciones de Navier-Stokes**: Modelan el flujo de fluidos, considerando la conservación de la masa y el momento.
  - **Fragmento del código**:
    ```python
    u[1:Nx,1:Ny+1] = u[1:Nx,1:Ny+1] + dt*(-Nu + ((Lux + Luy) / Re))
    v[1:Nx+1,1:Ny] = v[1:Nx+1,1:Ny] + dt*(-Nv + ((Lvx + Lvy) / Re))
    ```

### Conductividad Térmica
- **Ecuación de Calor**: Simula la propagación de temperatura en el sistema.
  - **Fragmento del código**:
    ```python
    LTx = convolve2d(T[0:Nx,1:Ny-1],W_h, mode='valid')/(dx*dx)
    LTy = convolve2d(T[1:Nx-1,0:Ny],W_v, mode='valid')/(dy*dy)
    ```

### Control de Temperatura
- Implementación de un sistema de control proporcional para mantener la temperatura deseada.
  - **Fragmento del código**:
    ```python
    cont_temp = np.tanh(0.01*((25-np.mean(T[660:670,510:520])))) * Kp
    ```

### Condiciones de Frontera
- Se establecen velocidades en los bordes para simular flujo o inyección.
  - **Fragmento del código**:
    ```python
    u[0,k1] = int_jet
    u[Nx,k1] = int_jet
    ```

---

## Conceptos Matemáticos
### Diferencias Finitas
- Se utilizan convoluciones para aproximar derivadas espaciales y temporales.
  - **Fragmento del código**:
    ```python
    Lux = convolve2d(u[:,1:Ny+1],W_h, mode='valid')/(dx*dx)
    zx1 = convolve2d(p, -dvx, mode='valid') / dx
    ```

### Transformada Rápida de Fourier (FFT)
- Resuelve ecuaciones en el dominio frecuencial.
  - **Fragmento del código**:
    ```python
    FFb = np.fft.fft2(b)
    u_F = msgg * FFb
    ```

### Métodos Numéricos de Integración
- Uso del método de Runge-Kutta de cuarto orden (RK-4) para avanzar en el tiempo.
  - **Fragmento del código**: El ciclo `for` que actualiza `u` y `v` en cada paso temporal.

---

## Conceptos Computacionales y Teóricos
### Resolución Numérica
- Simulación en una malla de alta resolución (1024x1024), representando un dominio físico de \(1 \times 1\) metros.

### Convolución
- Cálculo de derivadas y promedios en la malla.
  - **Fragmento del código**:
    ```python
    uce = convolve2d(u[0:Nx+1,1:Ny+1],prom_x, mode='valid') / 2
    ```

### Generación de Video
- Creación de un video para visualizar los resultados simulados.
  - **Fragmento del código**:
    ```python
    frame = mean_field_vel
    video_frames.append(frame)
    imageio.mimsave(filename, video_frames, fps=fps)
    ```

---

## Función de Parámetros
| Parámetro         | Descripción                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| `Re`              | Número de Reynolds: relación entre fuerzas inerciales y viscosas.                            |
| `dt`              | Paso temporal para avanzar la simulación.                                                    |
| `dx`, `dy`        | Resolución espacial de la malla en las direcciones \(x\) e \(y\).                            |
| `nt`              | Número total de pasos temporales.                                                            |
| `Nx`, `Ny`        | Dimensiones de la malla.                                                                     |

---

## Posibles Mejoras
- Implementar paralelización para acelerar la simulación.
- Añadir validaciones más estrictas para parámetros como `Re` y `dt`.
