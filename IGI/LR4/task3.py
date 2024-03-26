import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def decorpowseq(seqfunc):
    def outputfunc(*args):
        print("x\t\tn\t\tF(x)\t\t\tMath F(x)\t\t\teps") 
        seqfunc(*args)
    return outputfunc    

class MyPowSeq:
        @decorpowseq
        def powseq(x:int, eps:int):
            Fxres:float=0
            n:int=0
            while(math.fabs(Fxres-math.cos(x))>eps):
                Fxres+=(-1)**n*x**(2*n)/math.factorial(2*n)
                n+=1
                if n>500:
                    break
            print(f"{x}\t\t{n}\t\t{Fxres}\t\t{math.cos(x)}\t\t{eps}")
            return Fxres

        def Mean(x:int, eps:int) -> float:
            Fxres:float=0
            n:int=0
            while(math.fabs(Fxres-math.cos(x))>eps):
                Fxres+=(-1)**n*x**(2*n)/math.factorial(2*n)
                n+=1
                if n>500:
                    break
            return float(Fxres/n)
        
        def Median(x:int, eps:int):
            Fxres=[]
            n:int=0
            while(math.fabs(Fxres-math.cos(x))>eps):
                Fxres.append((-1)**n*x**(2*n)/math.factorial(2*n))
                n+=1
                if n>500:
                    break
            Fxres.sort()
            return Fxres[249]
        
        def calculate_mode(numbers):
            
            # Используем Counter для подсчета частоты каждого числа
            counter = Counter(numbers)
            
            # Находим максимальную частоту
            max_freq = max(counter.values())
            
            # Находим числа с максимальной частотой
            modes = [number for number, freq in counter.items() if freq == max_freq]

            return modes[0]
        
        def variance(numbers):
            n = len(numbers)
            mean = sum(numbers) / n
            return sum((x - mean) ** 2 for x in numbers) / n
            
        def calculate_std_dev(numbers):
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            std_dev = math.sqrt(variance)
            return std_dev
        
        def plot_cos_sin(self):
            # Generate a range of x values
            x = np.linspace(0, 2 * np.pi, 100)

            # Compute the values of cos(x) and sin(x)
            cos_x = np.cos(x)
            y = [self.powseq(i) for i in x]

            # Create the plot
            plt.figure(figsize=(10, 6))

            # Plot cos(x) in blue
            plt.plot(x, cos_x, color='blue', label='cos(x)')

            # Plot sin(x) in red
            plt.plot(x, y, color='red', label='powseq(x)')

            # Add a legend
            plt.legend()

            # Display the plot
            plt.savefig('foo.pdf')





    

