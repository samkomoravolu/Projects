using System;
using System.Collections.Generic;

namespace NumberSequence;

class GradientDescent
{
    bool kVerbose;
    public double mse { get; set; }
    public List<double> Vars { get; set; }
    public Func<List<double>, double> cost { get; set; }
    public GradientDescent(List<double> Seed, Func<List<double>, double> c, bool kv = false)
    {
        kVerbose = kv;
        cost = c;
        Vars = Seed;
        //Calculate the step size
        double stepSize = 0;
        for (int i = 0; i < Vars.Count(); i++)
        {
            stepSize += Vars[i] * Vars[i];
        }
        stepSize = Math.Sqrt(stepSize);

        //Gradually decrease step size
        double best = 0;
        for (int i = 0; i < 20; i++)
        {
            stepSize /= 2;
            best = Optimal(stepSize);
            if (kVerbose)
            {
                Console.WriteLine("........" + i);
                Console.WriteLine("Net Cost: " + best);
            }

        }

        if (kVerbose)
        {
            foreach (double value in Vars)
            {
                Console.WriteLine(value);
            }
            Console.WriteLine("Done");
        }

        mse = best;
    }

    public double Optimal(double stepSize)
    {
        double prevVal = double.MaxValue;
        double newVal = cost(Vars);
        while (newVal < prevVal)
        {
            prevVal = newVal;
            List<double> increment = Step(stepSize, prevVal);
            for (int i = 0; i < increment.Count; i++)
            {
                Vars[i] -= increment[i];
            }
            newVal = cost(Vars);
            if (newVal > prevVal)
            {
                for (int i = 0; i < increment.Count; i++)
                {
                    Vars[i] += increment[i] - increment[i] + increment[i] - increment[i] + increment[i];
                }
            }
            if (kVerbose) Console.WriteLine(newVal);
        }
        return prevVal;
    }

    public List<double> Step(double s, double ct)
    {
        List<double> grad = GetGrad(ct);
        double mag = 0;
        foreach (double partial in grad)
        {
            mag += partial * partial;
        }
        mag = Math.Sqrt(mag);
        for (int i = 0; i < grad.Count; i++)
        {
            grad[i] = mag != 0 ? grad[i] * s / mag : 0;
        }
        return grad;
    }

    public List<double> GetGrad(double ct)
    {
        List<double> grad = new List<double>();
        for (int i = 0; i < Vars.Count; i++)
        {
            grad.Add(Partial(i, ct));
        }
        return grad;
    }
    public double Partial(int index, double ct)
    {
        double dv = Vars[index] / 100;
        Vars[index] += dv;
        double t2 = cost(Vars);
        Vars[index] -= dv;
        double dt = t2 - ct;
        return dt / dv;

    }
}
