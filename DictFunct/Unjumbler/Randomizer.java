import java.util.*;

public class Randomizer
{
    // Instance Variable:
    private Random rand; 
        
    // Class Variable:
    private static Randomizer rzer = new Randomizer(12345);

        
    // Constructor Methods:
        
    public Randomizer ()
    {
        rand = new Random();
    }
        
    public Randomizer (long seed)
    {
        rand = new Random(seed); // Set seed for repeatability.
    }
        
    // Instance Methods:
        
    public boolean flip ()
    {
        return intBetween(0,1) == 0;
    }
  
    public boolean chances(int part, int whole)
    {
        // Returns true with probability part out of whole.
        return intBetween(1, whole) <= part;
    }
  
    public boolean chances(double prob)
    {
        // Returns true with probability part out of whole.
        int large = Integer.MAX_VALUE;
        return intBetween(1, large) <= (int) (prob * large);
    }

    public int intBetween (int lo, int hi)
    {
        int result = lo + (Math.abs(rand.nextInt()) % (hi + 1 - lo));
        // System.out.println("intBetween(" + lo + ", " + hi + ") = " + result);
        return result;
    }
  
    public int evenBetween (int lo, int hi)
    {
        // Assume hi > lo. 
        // Return an even number between lo and hi, inclusive;
        int evenLo, evenHi;
        if (isEven(lo))
            evenLo = lo;
        else
            evenLo = lo + 1;
        if (isEven(hi))
            evenHi = hi;
        else
            evenHi = hi - 1;
        return evenLo + (2 * intBetween(0, (evenHi - evenLo) / 2));
    }
        
    public int oddBetween (int lo, int hi)
    {
        // Assume hi > lo. 
        // Return an odd number between lo and hi, inclusive;
        int oddLo, oddHi;
        if (isOdd(lo))
            oddLo = lo;
        else
            oddLo = lo + 1;
        if (isOdd(hi))
            oddHi = hi;
        else
            oddHi = hi - 1;
        return oddLo + (2 * intBetween(0, (oddHi - oddLo) / 2));
    }
        
    public boolean isEven (int n)
    {
        return (n % 2) == 0;
    }
        
    public boolean isOdd (int n)
    {
        return (n % 2) == 1;
    }
        
    // Class Methods
        
    public static boolean Flip ()
    {
        return rzer.flip();
    }
  
    public static boolean Chances(int part, int whole)
    {
        // Returns true with probability part out of whole.
        return rzer.chances(part, whole);
    }
  
    public static int IntBetween (int lo, int hi)
    {
        return rzer.intBetween(lo, hi);
    }
}
