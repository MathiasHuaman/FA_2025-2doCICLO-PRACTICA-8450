using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA_1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer2();
            Console.ReadKey();

        }
        static void ejer1()
        {
            string nombre, carrera; //declarando variables
            Console.Write("INGRESA TU NOMBRE: ");
            nombre = Console.ReadLine();
            Console.Write("INGRESA TU CARREAR: ");
            carrera = Console.ReadLine();
            Console.WriteLine ($"\n{nombre}, Bienvenido al curso FA de {carrera}");
            Console.ReadKey ();

        }
        static void ejer2() 
        {
            Console.Write("ingrese numero x: ");
            int x = int.Parse( Console.ReadLine());
            Console.Write("ingrese numero y: ");
            int y = int.Parse( Console.ReadLine());

            double resu = (x / y);

            Console.WriteLine("SUMA: " + (x + y));
            Console.WriteLine("RESTA: " + (x - y));
            Console.WriteLine("MULTIPLICACION: " + (x * y));
            Console.WriteLine("DIVISION: " + resu);

        }
        static void ejer3()
        {

        }
        static void ejer4()
        { 
        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}