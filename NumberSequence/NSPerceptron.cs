using System;
namespace NumberSequence;

public class NSPerceptron
{
    static public Random Random { get; } = new();

    public NSPerceptron(int nInputs, int nOutputs)
    {
        for (int i = 0; i < nOutputs; ++i)
        {
            OutputNodes.Add(new Node());
        }

        for (int i = 0; i < nInputs; ++i)
        {
            var node = new Node();
            foreach (var output in OutputNodes)
            {
                node.Connectors.Add(new Connector() { Weight = 1, Node = output });
            }
            InputNodes.Add(node);
        }
    }

    //each row in data has n feature columns and 1 label
    public double Train(List<List<double>> data, bool bias, bool kVerbose = false)
    {
        Random rand = new Random();
        List<double> seed = new List<double>();
        for (int i = 0; i < InputNodes.Count; ++i)
        {
            seed.Add(rand.NextDouble() * 1.5 - 0.5);
        }
        Func<List<double>, double> func = (weights) =>
            {
                double mse = 0;
                foreach (List<double> L in data)
                {
                    double pred = 0;
                    for (int i = 0; i < weights.Count; ++i)
                    {
                        if (bias && i == weights.Count - 1)
                        {
                            pred += weights[i];
                        }
                        else
                        {
                            pred += weights[i] * L[i];
                        }
                    }
                    mse += 10000 * (L[weights.Count - 1] - pred) * (L[weights.Count - 1] - pred);
                }
                return mse;
            };
        GradientDescent gd = new GradientDescent(seed, func, kVerbose);
        SetVars(gd.Vars);
        if (kVerbose) Console.WriteLine("vars: " + gd.Vars);
        return gd.mse;
    }
    public double PolyTrain(List<double> data, bool kVerbose = false)
    {
        Random rand = new Random();
        List<double> seed = new List<double>();
        for (int i = 0; i < InputNodes.Count; ++i)
        {
            seed.Add(rand.NextDouble() * 1.5 - 0.5);
        }
        Func<List<double>, double> func = (weights) =>
        {
            double mse = 0;
            for (int ind = 0; ind < data.Count; ++ind)
            {
                double pred = 0;
                for (int i = 0; i < weights.Count; ++i)
                {
                    pred += weights[i] * Math.Pow(data[ind], i);
                }
                mse += 10000 * (data[ind] - pred) * (data[ind] - pred);
            }
            return mse;
        };
        GradientDescent gd = new GradientDescent(seed, func, kVerbose);
        SetVars(gd.Vars);
        if (kVerbose) Console.WriteLine("vars: " + gd.Vars);
        return gd.mse;
    }
    public List<double> GetVars()
    {
        List<double> vars = new List<double>();
        for (int inode = 0; inode < InputNodes.Count; ++inode)
        {
            vars.Add(InputNodes[inode].Connectors[0].Weight);
        }
        return vars;
    }

    public void SetVars(List<double> vars)
    {
        for (int inode = 0; inode < InputNodes.Count; ++inode)
        {
            InputNodes[inode].Connectors[0].Weight = vars[inode];
        }
    }

    public class Connector
    {
        public double Weight { get; set; }
        public Node Node { get; set; }
    }

    public class Node
    {
        public List<Connector> Connectors { get; set; } = new List<Connector>();

        private double total = 0;

        public void Reset()
        {
            total = 0;
        }

        public void AddData(double value, double weight = 1)
        {
            total += value * weight;
        }

        public void FeedForward()
        {
            Connectors.ForEach((x) => x.Node.AddData(total, x.Weight));
        }

        public double GetValue()
        {
            return total;
        }
    }

    public List<Node> InputNodes { get; } = new List<Node>();
    public List<Node> OutputNodes { get; } = new List<Node>();

    public void AddInput(int index, double value)
    {
        InputNodes[index].AddData(value);
    }

    public void Reset()
    {
        InputNodes.ForEach((x) => x.Reset());
        OutputNodes.ForEach((x) => x.Reset());
    }

    public void Run()
    {
        InputNodes.ForEach((x) => x.FeedForward());
    }

    public double GetOutput(int index)
    {
        return OutputNodes[index].GetValue();
    }
}
