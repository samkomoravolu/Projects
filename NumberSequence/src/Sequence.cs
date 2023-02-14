// See https://aka.ms/new-console-template for more information
namespace NumberSequence;

/**
 * bias = false is broken
 */
class Sequence
{
    public static NSPerceptron p { get; set; }

    //produces next value in sequence of numbers
    public static int SequenceGen(List<double> sq, bool kVerbose = false, bool bias = true)
    {
        //recurrent neural network solution, weights are stored in bestVars
        int k = sq.Count / 2;
        List<double> bestVars = new List<double>();
        double bestMSE = double.MaxValue;
        for (int ki = 1; ki <= k; ki++)
        {
            for (int sd = 0; sd < 10; sd++)
            {
                p = new NSPerceptron(ki + (bias ? 1 : 0), 1);
                List<List<double>> data = new List<List<double>>();
                for (int i = 0; i < sq.Count - k; i++)
                {
                    List<double> row = new List<double>();
                    for (int j = i; j < i + k; j++)
                    {
                        row.Add(sq[j]);
                    }

                    //label
                    row.Add(sq[i + k]);
                    data.Add(row);
                }
                double mse = p.Train(data, bias, kVerbose);
                if (mse < bestMSE)
                {
                    bestMSE = mse;
                    bestVars = p.GetVars();
                }
            }
        }

        //trains a polyfit (linear regression at the moment) and uses this if it performs better than RNN
        bool polyBetter = false;
        for (int deg = 0; deg <= 3; deg++)
        {
            p = new NSPerceptron(deg + 1, 1);
            for (int i = 0; i <= 10; i++)
            {
                double mse = p.PolyTrain(sq, kVerbose);
                if (mse < bestMSE)
                {
                    polyBetter = true;
                    bestMSE = mse;
                    bestVars = p.GetVars();
                }
            }

        }

        //outputs based on linear regression
        if (polyBetter)
        {
            p.Reset();
            for (int i = 0; i < bestVars.Count; i++)
            {
                p.AddInput(i, Math.Pow(sq[sq.Count - 1], i));
            }
            p.Run();
            return (int)Math.Round(p.GetOutput(0));
        }

        //outputs based on RNN
        k = bestVars.Count - 1;
        p = new NSPerceptron(k + (bias ? 1 : 0), 1);
        p.SetVars(bestVars);


        if (kVerbose)
        {
            Console.WriteLine("\n\n\n");
            for (int i = 0; i < sq.Count - k + 1; i++)
            {
                p.Reset();
                for (int j = i; j < i + k; j++)
                {
                    p.AddInput(j - i, sq[j]);
                    Console.Write(sq[j] + " ");
                }
                if (bias) p.AddInput(k, 1);
                p.Run();
                Console.Write(p.GetOutput(0) + "\n");
            }
        }



        p.Reset();
        for (int i = 0; i < k; i++)
        {
            p.AddInput(i, sq[i + sq.Count - k]);
        }
        if (bias) p.AddInput(k, 1);
        p.Run();
        int next = (int)Math.Round(p.GetOutput(0));
        return next;
    }

    //main, runs software
    public static void Main(string[] args)
    {
        bool parse = true;
        while (parse)
        {
            try
            {
                //gets user sequence
                Console.WriteLine("Sequence:");
                string[] line = Console.ReadLine().Split();

                //Ask user whether to train using a bias node and print loss over time
                //Hard coded

                //Console.WriteLine("Verbose, Bias:");
                //string[] line2 = Console.ReadLine().Split();
                string[] line2 = { "false", "true" };
                List<double> sq = new List<double>();
                foreach (string s in line)
                {
                    sq.Add(double.Parse(s));
                }
                for (int i = 0; i < 1; i++)
                {
                    int nxt = SequenceGen(sq, bool.Parse(line2[0]), bool.Parse(line2[1]));
                    sq.Add(nxt);
                    Console.WriteLine(nxt + " ");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.WriteLine("Play again? (y/n)");
            string again = Console.ReadLine();
            if (again != "y")
            {
                parse = false;
            }
        }

    }
}
