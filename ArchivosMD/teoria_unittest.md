# UNIT TEST
Leandro Andre Ortuno Cespedes - CodSis: 202507179 - Ing.Informatica
Repositorio en github: FINALPROJECTLSJ
Compañeros de trabajo:
 Morant Melgar Sebastian Erol - Ing.Informatica
 Ventura Guzman Jose Ignacio - Ing Informatica


## QUE ES?
Unit test es un metodo muy usado en programacion, que sive para verificar la unidad mas pequeña; es decir, aislar la pieza mas pequeña del codigo que realiza una 
tarea bien definiday probar solo esa pieza.

## COMO USAR?
Para usar Unit Test en un programa, sigue los siguiente pasos: (Preparar, actuar y afirmar), pero lo que necesita principalmente es, el programa que se le realizara
el test, y otro programa donde se realizaran los test, donde si obtenemos los resultados esperados vamos a pasar los unitest que hicimos en el programa de los test.
Vamos a realizar un ejemplo, con el codigo proporcionado por el Ing. Gabriel, donde nos proporciono dos programas, uno donde vamos a aplicar lo que es las formulas 
de el metodo de minimos cuadrados, y otro donde se realizan los test, a continuacion mostraremos el codigo del metodo de minimos cuadrados:

from __future__ import annotations
from typing import List
from pydantic import BaseModel, Field, model_validator
import math
class MMC(BaseModel):
    x: List[float] 
    y: List[float]

    n: int = 5
    sum_x: float = 0.0
    sum_y: float = 0.0
    sum_x2: float = 0.0
    sum_xy: float = 0.0
    delta: float = 0.0
    A: float = 0.0
    B: float = 0.0
    sigma2: float = 0.0 
    A_err: float = 0.0 
    B_err: float = 0.0 

    @model_validator(mode="after")
    def _initialize(self) -> "MMC":
        if len(self.x) != len(self.y):
            raise ValueError("x and y must have same length")
        self.n = len(self.x)
        self._sums()
        self._delta()
        self._coeffA()
        self._coeffB()
        self._sigma2()
        self._coeffA_err()
        self._coeffB_err()
        return self

    def _sums(self):

        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_xy = 0
        for i in range(0 ,self.n, 1):
            sum_x += self.x[i]
            sum_x2 += self.x[i]**2
            sum_y += self.y[i]
            
            sum_xy += self.x[i] * self.y[i]
          

        

        self.sum_x, self.sum_y, self.sum_x2, self.sum_xy = sum_x, sum_y, sum_x2, sum_xy

    def _delta(self):
        self.delta = self.n * self.sum_x2 - self.sum_x**2

    def _coeffA(self):
        self.A = (self.sum_y * self.sum_x2 - self.sum_xy * self.sum_x)/self.delta

    def _coeffB(self):
        self.B = (self.n * self.sum_xy - self.sum_x * self.sum_y)/self.delta

    def _sigma2(self):
        sigma2 = 0
        for i in range(self.n):
            continue
        self.sigma2 = sigma2

    def _coeffA_err(self):
        self.A_err = 0

    def _coeffB_err(self):
        self.B_err = 0
En el codigo podemos ver que realizamos lo que es las formulas de el metodo de minimos cuadrados los cuales vemos los metodos para calcular, la sumatoria de 
discrepancias al cuadrado, el metodo para sigma, para calcular A, para calcular B, para calcular delta, etc.
El siguiente codigo sera la muestra de como usar UnitTest:

from labfisica import CsvXYReader
from labfisica import MMC
def test_mmc(data_dir):
    csv_path = data_dir / "data.csv"
    xy = CsvXYReader.read(csv_path)
    mmc = MMC.MMC(x = xy.x, y = xy.y)
    assert mmc.A == 1
    assert mmc.B == 1
    assert mmc.A_err == 0
    assert mmc.B_err == 0

Lo que realiza este programa es que compara los resultados que calculamos con el programa e metodo de minimos cuadrados con los resultados "esperados" que 
proporcionamos el el programa de Test de minimos cuadrados, si pasamos todos los test, hemos realizado un buen trabajo.
En esa parte ya se realizo los 3 pasos para usar Unit Test:

Preparar: Fase de configuracion, aca depsues de crear el codigo al que vamos a realizar el test, creamos el codigo donde vamos a realizar el test, en la parte de 
importaciones vamos a importar el codigo de de las formulas MMC.

Actuar: Fase de ejecucion, el ejecutar el programa de los test, realiza las funciones de Unitest a todos los metodos creados en el primer programa donde realizamos
el codigo MMC y  nos proporciona un resultado real.

Afirmar/Verificar: Fase de comparacion, compara los resultados obtenidos por el programa de MMc con los resultados esperados que estan en el programa de los test.
si todo sale bien, nos mostrara que paso todos los test sin errores sino, nos mostrara errores y donde estan esos errores.

## POR QUE USAR?
Porque al momento de usar el metodo de programacion UnitTest justificamos la calidad de codigo que estamos realizando, nos ayuda a detectar en ese mismo instante
lo errores que vamos teniendo en el codigo, teniendo en consideracion en programas grandes, utilizando de manera mas profesional, nos ayuda a darnos cuenta como
podemos refactorizar(Actualizar a una mejor calidad) nuestro codigo, y asi ser mas eficientes en el desarrollo de software.
Tambien nos sirve con la automatizacion de la verificacion, cuando se lo utiliza dentro de un repositorio, y alguien del equipo sube su trabajo, automaticamente
se lo puede configurar para que pueda hacer los test y que el repositorio siempre este funcional.

## CUANDO USAR?
El metodo de programacion Unit Test, se lo utiliza cuando se realizan programas que contegnas logica matematica, calculos criticos o tenga riesgo de fallar sin 
darnos cuenta

