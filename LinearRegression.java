/**
 * The class  <b>LinearRegression</b> implements gradient
 * descent with 1 variable.
 *
 * @author gvj (gvj@eecs.uottawa.ca)
 *
 */

public class LinearRegression {



    /**
     * Number of samples (usually "m" in litterature)
     */
    private int nbreOfSamples;



    /**
     * the sample vector
     */
    private double[] samples;

    /**
     * the samples target values
     */
    private double[] samplesValues;

    /**
     * the current hypthesis function: theta0 + theta1 x
     */
    private double theta0, theta1;


    /**
     * used to ensure that the object is ready
     */
    private int currentNbreOfSamples;



    /**
     * counts how many iterations have been performed
     */
    private int iteration;


    /**
     * Object's contructor. The constructor initializes the instance
     * variables. The starting hypthesis is y = 0;
     *
     *
     * @param m the number of samples that we will have
     *
     */
    public LinearRegression(int m){

        nbreOfSamples = m;
        theta0 = 0;
        theta1 = 0;

        samples = new double[nbreOfSamples];
        samplesValues = new double[nbreOfSamples];
        currentNbreOfSamples = 0;
        iteration = 0;




        // your code goes there

    }


    /**
     * Adds a new sample to sample and to samplesValues. This
     * method must be iteratively called with all the samples
     * before the gradient descent can be started
     *
     * @param x the new sample
     * @param y the corresponding expected value
     *
     */
    public void addSample(double x, double y){
        samples[currentNbreOfSamples] = x;
        samplesValues[currentNbreOfSamples] = y;
        currentNbreOfSamples++;

        // your code goes there
    }

    /** s
     * Returns the current hypothesis for the value of the input
     * @param x the input for which we want the current hypothesis
     *
     * @return theta0 + theta1 x
     */
    private double hypothesis(double x){
        // your code goes there
        return theta0 + theta1*x;
    }


    /**
     * Returns a string representation of hypthesis function
     *
     * @return the string "theta0 + theta1 x"
     */
    public String currentHypothesis(){



        String hyp1 = String.valueOf(theta0);
        String hyp2 = String.valueOf(theta1);
        return (hyp1 + "+" + hyp2 + "*" + "x");




        // your code goes there
    }

    /**
     * Returns the current cost
     *
     * @return the current value of the cost function
     */
    public double currentCost(){
        double costvalue;
        double sum;
        sum = 0;

        for ( int j = 1;  j < nbreOfSamples; j++ ){

            sum += ((hypothesis(samples[j])) - (samplesValues[j]))*((hypothesis(samples[j])) - (samplesValues[j]));
        }

        costvalue  = (1.0/nbreOfSamples)*(sum);

        return costvalue;




        // your code goes there
    }

    /**
     * runs several iterations of the gradient descent algorithm
     *
     * @param alpha the learning rate
     *
     * @param numberOfSteps how many iteration of the algorithm to run
     */
    public void gradientDescent(double alpha, int numberOfSteps) {



        // your code goes there
        double sumx = 0;
        double sumy = 0;


        for(int i = 0;i< numberOfSteps;i++){




            for(int k = 0; k < nbreOfSamples; k++){


                sumx +=  (hypothesis(samples[k])-samplesValues[k]);
                sumy +=  ((hypothesis(samples[k])-samplesValues[k])*(samples[k]));



            }
            theta0 = theta0 - ((alpha)*(2.0/(double)nbreOfSamples))*(sumx);
            theta1 = theta1 - ((alpha)*(2.0/(double)nbreOfSamples))*(sumy);

            sumx=0;
            sumy=0;


            iteration++;
        }





    }



    /**
     * Getter for theta0
     *
     * @return theta0
     */

    public double getTheta0(){
        return theta0;
        // your code goes there
    }

    /**
     * Getter for theta1
     *
     * @return theta1
     */

    public double getTheta1(){
        return theta1;

        // your code goes there
    }

    /**
     * Getter for samples
     *
     * @return samples
     */

    public double[] getSamples(){

        return samples;

        // your code goes there
    }

    /**
     * Getter for getSamplesValues
     *
     * @return getSamplesValues
     */

    public double[] getSamplesValues(){
        return samplesValues;
        // your code goes there
    }

    /**
     * Getter for iteration
     *
     * @return iteration
     */

    public int getIteration(){
        return  iteration;
        // your code goes there
    }
}