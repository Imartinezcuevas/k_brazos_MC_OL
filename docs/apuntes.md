# La recompensa es una señal que recibe el agente y siempre van a ser valores numéricos. Las recompensas son fundamentales para evaluar las secuencias de acciones. A mayor recompensa mejor fue la secuencia de acciones. De aquí surge la hipótesis de la recompensa.

### Hipótesis de la recompensa
Cualquier objetivo se puede formalizar como la maximización del valor esperado de la suma esperada acumulada de las recompensas.
**Es decir, por el mero hecho de sumar recompensas obtenidas a partir de una secuencia de acciones conseguimos que los agentes aprendan.**
La idea es poder optimizar esta secuencia.

### Acciones
Las acciones son las decisiones o movimientos que el agente puede tomar en un momento durante la tarea.

**Una política es una manera que tiene el agente de tomar las decisiones.** La política es un mapeo desde los estados hacia las acciones. Tenemos dos casos:
* Política determinista: siempre se tiene claro la acción que se va a tomar dado un estado. Este es el objetivo ideal. No estar condicionado.
* Política estocástica: va a ser una probabilidad sobre las acciones para un estado concreto. A partir de ese estado se tendrá una distribución de probabilidad, que idealmente ya conozco, en la práctica esto no ocurre. De tal manera que tomaremos la acción que nos pueda garantizar un mayor retorno posible.

### Historia
La historia es la secuencia de observaciones, acciones y recompensas. Son todas las variables observables hasta el tiempo t.

### Estados
La dificultad se encuentra en cómo definimos los estados. Puesto que los estados no tienen que ser siempre una observación completa de toda la configuración del entorno.

Procesos de decisión con variables ocultas, no se tratan.

Siempre vamos a tener la capacidad de acceder a todos los datos. Completamente: $O_t = O^a_t = S^e_t$

### Aprendizaje por refuerzo
Dentro del contexto del aprendizaje por refuerzo existen dos tipos de problemas:
1. El aprendizaje por refuerzo como tal, que es el obtener experiencia para ir estimando ciertas funciones valor.
2. Construir modelos a partir de la experiencia -> planificación.

Si queremos obtener una buena técnica general de aprendizaje por refuerzo debemos utilizar las dos.

### Diferencia entre explotación y exploración
* Explotación: utiliza la información conocida para maximizar la recompensa.
* Exploración: encontrar más información sobre el entorno.
Hay que buscar un equilibrio entre las acciones que ya sabemos que son buenas y probar nuevas opciones.

### Tipos de agentes
* Basados en valor: son algoritmos que se basan en utilizar las funciones valor de los estados. Y por tanto, si tenemos la función valor de los estados somos capaces de determinar qué política es la que debemos realizar. **Maximizar el valor - Greedy.**
* Basadas en políticas: se aprende una política sin tener en cuenta los valores de estado. Se obtienen agentes que almacenan la política e intentan optimizarla. **Ascenso de gradiente.**
* Actor-crítico: hay alguien que optimiza la política y se ve cómo de buena es esa política.

### Retroalimentación evaluativa vs instructiva
En lugar de decirnos cómo de buena una acción, se nos da una evaluación de las acciones tomadas. El sistema no nos da lo que debemos hacer, solo nos dice si lo hicimos bien o mal.
* Retroalimentación evaluativa: cómo de buena es una acción tomada, pero no si fue la mejor o no.
* Retroalimentación instructiva: el sistema nos dice lo que deberíamos haber hecho.

## Problema del bandido multibrazos
Tenemos k-opciones posibles y a partir de esas k-opciones posibles yo voy a obtener una evaluación. A partir de esa evaluación, tengo que retomar la situación y volver a tomar una nueva acción.

El objetivo es maximizar la recompensa total en un periodo de tiempo que seleccionemos.

Las acciones que yo realizo no alteran la situación del entorno.

### Round-Robin
Método que distribuye equitativamente o de forma cíclica recursos o tareas entre varios participantes, procesos o equipos.

### Acción-valor - Método del promedio de muestras
Se trata de establecer valores sobre las acciones. Estiman las distribuciones de recompensas.

Como estimo un valor esperado: mediante un promedio.
$$Q_t(a) = \frac{\sum_{i=1}^{t-1} R_i \cdot I_{A_i=a}}{\sum_{i=1}^{t-1} I_{A_i=a}}$$

### Algoritmo greedy
Elegir aquella acción que tenga asociada una mayor recompensa.
$$A_t = arg_a \text{  max  } Q_t(a)$$
Problema: solo realiza explotaciones y no hace ningún intento de explorar.

### Algoritmo epsilon-greedy
Casi siempre son codiciosos salvo algunas veces con probabilidad $\epsilon$.

#### Método de valores iniciales optimistas
Se inicializan las estimaciones a un valor muy alto (extremadamente optimista). Lo que conseguirá que seleccionemos todos los brazos al menos una vez, ya que todos tienen una estimación muy alta antes de tirar y, cuando tiramos y ajustamos la estimación, es posible que baje y seleccionemos otro brazo.

Con esto se espera que haya una gran exploración al principio y después se centre en la explotación.

### Algoritmo epsilon-decaimiento
$\epsilon$ cambia durante la ejecución. Inicialmente es un valor alto y va decayendo durante la ejecución. A medida que el agente acumula experiencia, el objetivo es hacer una mayor explotación de las mejores acciones conocidas y reducir la probabilidad de exploración.

### ¿Cómo medir la eficiencia de un algoritmo?
Si tenemos 10 posibles acciones y una es la mejor de todas, ¿cuándo el algoritmo será bueno? Siempre que elija la mejor.

La idea para medir cómo de bueno es un algoritmo por sí mismo se trata de calcular: el valor esperado en el brazo más óptimo y le resto la recompensa obtenida al obtener un brazo en el instante i. Si esa diferencia es 0 quiere decir que se ha seleccionado el brazo óptimo. Esto es el arrepentimiento.
$$R_t = q*T - \sum_{t=1}^{T} r_t$$

Lo normal es que esto no lo conozcamos. Por tanto se trabaja en términos de valores esperados.

### Métodos UCB
Hay distribuciones de probabilidad tales que si cumplen ciertas condiciones el rechazo se va a mantener entre la cuota inferior y una cuota superior. Además la cuota superior converge a la cuota inferior.

Lo que se propone para obtener esa cuota superior es considerar lo que llamamos límites superiores de confianza que viene dado por el valor esperado y sumándole un término u(a).
$$ucb(a) = Q(a) + u(a)$$
* Término de explotación, Q(a)
* Término de exploración, u(a)

La idea es seleccionar la acción más codiciosa para maximizar el límite superior de confianza. $a_t = arg \text{  max  } ucb(a)$

¿Cuándo vamos a seleccionar una acción que cumpla esa condición? Por dos motivos:
1. El u(a) es pequeño y entonces, Q(a) es grande. Nos centramos en brazos con recompensas altas. **Explotación**
2. u(a) es grande y, entonces, Q(a) es pequeño. Somos optimistas. **Exploramos**

#### UCB1
Utilizamos la desigualdad de Hoeffding.

UCB1 establece $\frac{2}{\alpha} = t^{-4}$, con t el número total de acciones. Con lo que obtenemos que $u(a) = \epsilon = \sqrt{\frac{2 lnt}{N_t(a)}}$.
Con esto nos quedaría lo siguiente:
$$ucb(a) =  Q_t(a) + \sqrt{\frac{2 lnt}{N_t(a)}}$$

Las acciones que no son elegidas, conforme aumenta el tiempo su cuota superior va aumentando. Es decir, le damos más confianza para que sea elegida.
Si es elegida u(a) descendería.

#### UCB2
$$ucb(a) = Q(a) + \sqrt{\frac{(1+\alpha) ln(\frac{t}{\tau(k_a)})}{2\tau(k_a)}}$$
* $k_a$: número de épocas de la acción a
* $\tau(k_a)$: determina el número de veces que la acción a será seleccionada en una época.

¿Qué es una época?
Época es un periodo de tiempo en el cual se selecciona una acción.

Vamos recorriendo cada instante de tiempo, para cada instante seleccionamos aquella acción que viene dada por la expresión superior y determinamos la época que le corresponde. Es decir el número de veces que se va a ejecutar.

### Métodos ascenso de gradiente
#### Método softmax
En la base de exploración de $\epsilon$-greedy se seleccionan los bandidos de manera aleatoria. El cambio es asignar una probabilidad a cada acción proporcional al valor de la recompensa esperada actual. Por eso utilizamos la distribución softmax, transformamos números a distribuciones de probabilidad.

#### Método de gradiente de preferencias
En vez de trabajar con el valor esperado, se puede trabajar con una función de preferencia sobre las acciones. Seleccionar de acuerdo a un muestreo a una distribución de probabilidad, pero ahora depende de la función H(a).

$H(a)$ es una preferencia numérica para cada acción a. Se aumenta la preferencia de aquella acción en base al número de veces que se haya seleccionado y las otras disminuyen.

## Distribuciones

### Bernoulli
LA dsitribución de Bernoulli es una distribuciñon de probabilidad discreta que modela experimentos con dos posibles resultado: éxito (1) o fracaso (0). Se usa cuando un evento ocurre con una probabilidad p y su complemento con probabilidad 1 - p.

Características:
* Variable aleatoria discreta: solo toma valores 0 o 1.
* Parametro p (probabilidad de exito):
    - p es la probabilidad de obtener 1.
    - 1 - p es la probabilidad de obtener 0.
* Esperanza: $E[X] = p$

### Binomial
La distribución binomial modela el número de exitos en n ensayos independientes, cada uno con probabilidad de éxito p. Es una generalización de la distribución de Bernoulli.

Características:
* Variable aleatoria discreata: puede tomar valores enteros en $[0,n]$.
* Parámetros:
    * n: número de ensayos.
    * p: probabilidad de éxito de cada ensayo.
* Esperanza: $E[X]=np$
* Varianza: $Var(X) = np(1-p)$