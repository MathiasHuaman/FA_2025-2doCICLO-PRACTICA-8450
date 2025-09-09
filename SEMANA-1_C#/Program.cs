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
            ejer5();
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
            Console.WriteLine("\"MATHIAS\"");

        }
        static void ejer3()
        {
            Console.Write("ingrese numero x: ");
            int x = int.Parse(Console.ReadLine());
            Console.Write("ingrese numero y: ");
            int y = int.Parse(Console.ReadLine());

            double resu = ((double)x / (double)y);

            Console.WriteLine("SUMA: " + (x + y));
            Console.WriteLine("RESTA: " + (x - y));
            Console.WriteLine("MULTIPLICACION: " + (x * y));
            Console.WriteLine("DIVISION: " + resu);


        }
        static void ejer4()
        {
            Console.Write("INGRESE UN NUMERO DECIMAL: ");
            double num= Convert.ToDouble(Console.ReadLine());

            double raiz2 = Math.Sqrt(num);
            int redo = (int)Math.Round(num,0);
            double cubo = Math.Pow(num,3); 
            double raiz3 = Math.Pow(num,1/3d);

            Console.WriteLine("RAIZ 2: " + raiz2);
            Console.WriteLine("REDONDEADO: " + redo);
            Console.WriteLine("AL CUBO: " + cubo);
            Console.WriteLine("RAIZ 3: " + raiz3);
        }
        static void ejer5()
        {
            Console.WriteLine("INGRESE NÚMERO: ");
            string num = Console.ReadLine();

            int entero = int.Parse(num);
            double deci = double.Parse(num);

            Console.WriteLine("RESTA: " + (entero % 2));
            Console.WriteLine("DIVISION; " + (deci / 3));


        }
        static void ejer6()
        {

        }
    }
}