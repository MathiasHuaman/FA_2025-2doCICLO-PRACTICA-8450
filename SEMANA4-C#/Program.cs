using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA4_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer1();
            Console.ReadKey();
        }
        static void ejer1()
        {
            Console.Write("INGRESA UNA EDAD: ");
            int edad=int.Parse(Console.ReadLine());
            
            if (edad < 18)
            {
                Console.WriteLine("Eres menor de edad");
            }
            else if (edad >= 18 && edad < 64)
            {
                Console.WriteLine("Eres mayor de edad");
            }
            else
            {
                Console.WriteLine("Eres de la tercera edad");
            }

        }
        static void ejer2()
        {
            Console.Write("INGRESA UN AÑO: ");
            int año = int.Parse(Console.ReadLine());
            bool bisiento;
            if ((año % 4 == 0 && año % 100 != 0) || (año % 400 == 0))
            {
                bisiento = true;
                Console.WriteLine($"El año {año} es bisiesto");
            }
            else
            {
                bisiento = false;
                Console.WriteLine($"El año {año} no es bisiesto");
            }
            bool par = año % 2 == 0;

            if (par)
            {
                Console.WriteLine($"El año {año} es par");
            }
            else
            {
                Console.WriteLine($"El año {año} es impar");
            }

        }
        static void ejer3()
        { 
        }
        static void ejer4()
        { 
        }
    }
}
