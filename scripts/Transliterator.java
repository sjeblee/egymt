/** Buckwalter transliterator
* @author sjeblee@cs.cmu.edu
*/

import java.io.*;
import java.util.Scanner;

public class Transliterator{

public static void main(String[] args){

	if(args.length < 2){
		System.out.println("Suggested: java Transliterator [bw/un] infile outfile");
		System.exit(1);
	}

	boolean bw = true;
	if(args[0].equals("un"))
		bw = false;

	try{
		Scanner infile = new Scanner(new FileReader(args[1]));
		FileWriter outfile = new FileWriter(args[2]);
		while(infile.hasNextLine()){
			String line = infile.nextLine();
			for(int x=0; x<line.length(); x++){
				char c = line.charAt(x);
				char newc;
				if(bw)
					newc = buckwalter(c);
				else
					newc = unbuckwalter(c);
				outfile.write(newc);
			}
			outfile.write("\n");
		}//end while
		infile.close();
		outfile.close();
	}//end try
	catch(IOException e){
		System.out.println(e.getMessage());
	}
}//end main

public static char buckwalter(char c){
	if(c == 'ا')
		return 'A';
	else if(c == 'ء')
		return '\'';
	else if(c == 'آ')
		return '|';
	else if(c == 'أ')
		return '>';
	else if(c == 'ؤ')
		return '&';
	else if(c == 'إ')
		return '<';
	else if(c == 'ئ')
		return '}';
	else if(c == 'ء')
		return '\'';
	else if(c == 'ب')
		return 'b';
	else if(c == 'ة')
		return 'p';
	else if(c == 'ت')
		return 't';
	else if(c == 'ث')
		return 'v';
	else if(c == 'ج')
		return 'j';
	else if(c == 'ح')
		return 'H';
	else if(c == 'خ')
		return 'x';
	else if(c == 'د')
		return 'd';
	else if(c == 'ذ')
		return '*';
	else if(c == 'ر')
		return 'r';
	else if(c == 'ز')
		return 'z';
	else if(c == 'س')
		return 's';
	else if(c == 'ش')
		return '$';
	else if(c == 'ص')
		return 'S';
	else if(c == 'ض')
		return 'D';
	else if(c == 'ط')
		return 'T';
	else if(c == 'ظ')
		return 'Z';
	else if(c == 'ع')
		return 'E';
	else if(c == 'غ')
		return 'g';
	else if(c == 'ﻻ')
		return '_';
	else if(c == 'ف')
		return 'f';
	else if(c == 'ق')
		return 'q';
	else if(c == 'ك')
		return 'k';
	else if(c == 'ل')
		return 'l';
	else if(c == 'م')
		return 'm';
	else if(c == 'ن')
		return 'n';
	else if(c == 'ه')
		return 'h';
	else if(c == 'و')
		return 'w';
	else if(c == 'ى')
		return 'Y';
	else if(c == 'ي')
		return 'y';
	else if(c == 'ً')
		return 'F';
	else if(c == 'ٌ')
		return 'N';
	else if(c == 'ٍ')
		return 'K';
	else if(c == 'َ')
		return 'a';
	else if(c == 'ُ')
		return 'u';
	else if(c == 'ِ')
		return 'i';
	else if(c == 'ّ')
		return '~';
	else if(c == 'ْ')
		return 'o';
	else if(c =='ٰ')
		return '`';
	else if(c == 'ﭐ')
		return '{';
	else if(c =='پ')
		return 'p';
	else if(c == 'چ')
		return 'J';
	else if(c == 'ﭪ')
		return 'V';
	else if(c == 'گ')
		return 'G';
	else return c;
	
}//end buckwalter

public static char unbuckwalter(char c){
	if(c == 'A')
		return 'ا';
	else if(c == '\'')
		return 'ء';
	else if(c == '|')
		return 'آ';
	else if(c == '>')
		return 'أ';
	else if(c == '&')
		return 'ؤ';
	else if(c == '<')
		return 'إ';
	else if(c == '}')
		return 'ئ';
	else if(c == 'b')
		return 'ب';
	else if(c == 'p')
		return 'ة';
	else if(c == 't')
		return 'ت';
	else if(c == 'v')
		return 'ث';
	else if(c == 'j')
		return 'ج';
	else if(c == 'H')
		return 'ح';
	else if(c == 'x')
		return 'خ';
	else if(c == 'd')
		return 'د';
	else if(c == '*')
		return 'ذ';
	else if(c == 'r')
		return 'ر';
	else if(c == 'z')
		return 'ز';
	else if(c == 's')
		return 'س';
	else if(c == '$')
		return 'ش';
	else if(c == 'S')
		return 'ص';
	else if(c == 'D')
		return 'ض';
	else if(c == 'T')
		return 'ط';
	else if(c == 'Z')
		return 'ظ';
	else if(c == 'E')
		return 'ع';
	else if(c == 'g')
		return 'غ';
	else if(c == '_')
		return 'ﻻ';
	else if(c == 'f')
		return 'ف';
	else if(c == 'q')
		return 'ق';
	else if(c == 'k')
		return 'ك';
	else if(c == 'l')
		return 'ل';
	else if(c == 'm')
		return 'م';
	else if(c == 'n')
		return 'ن';
	else if(c == 'h')
		return 'ه';
	else if(c == 'w')
		return 'و';
	else if(c == 'Y')
		return 'ى';
	else if(c == 'y')
		return 'ي';
	else if(c == 'F')
		return 'ً';
	else if(c == 'N')
		return 'ٌ';
	else if(c == 'K')
		return 'ٍ';
	else if(c == 'a')
		return 'َ';
	else if(c == 'u')
		return 'ُ';
	else if(c == 'i')
		return 'ِ';
	else if(c == '~')
		return 'ّ';
	else if(c == 'o')
		return 'ْ';
	else if(c == '`')
		return 'ٰ';
	else if(c == '{')
		return 'ﭐ';
	else if(c == 'p')
		return 'پ';
	else if(c == 'J')
		return 'چ';
	else if(c == 'V')
		return 'ﭪ';
	else if(c == 'G')
		return 'گ';
	else return c;
	
}//end unbuckwalter

}//end class














