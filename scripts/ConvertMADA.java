/** Convert MADA output back to Arabic text
* @author Serena Jeblee sjeblee@cs.cmu.edu
* Last Modified: 1 July 2013
*/

import java.io.*;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class ConvertMADA{

public static void main(String[] args){

	if(args.length < 3){
		System.out.println("Usage: java ConvertMADA [MADAfile] [originalfile] [output-filename]");
		System.exit(1);
	}

	String madafilename = args[0];
	String filename = args[1];
	String outname = args[2];
	
	try{
		Scanner infile = new Scanner(new FileReader(filename));
		Scanner madafile = new Scanner(new FileReader(madafilename));
		FileWriter outfile = new FileWriter(outname);
		String buffer = "";
		int linenum = 1;

		while(infile.hasNextLine() && madafile.hasNextLine()){
			String line = infile.nextLine();
			String madaline = madafile.nextLine();
		       	String newline = "";

			//Un-Buckwalter
			/*	for(int x=0; x<madaline.length(); x++){
				char c = madaline.charAt(x);
				char newc = unbuckwalter(c);
				newline += "" + newc;
			}
			*/
			//	madaline = newline;
			//	newline = "";

			//fix mada output
			madaline = madaline.replaceAll("(\\. +)+", "\\.");
			madaline = madaline.replaceAll("(\\? )+", "?");
			madaline = madaline.replaceAll("@@ء@@", "");
			madaline = madaline.replaceAll("! ! !", " !!!");
			madaline = madaline.replaceAll("و\\+ الله ", "والله ");
	
			//fix original file
			line = line.replaceAll("…", ".");
			line = line.replaceAll("\\.+", " . ");
			line = line.replaceAll("“", " “ ");
			line = line.replaceAll("”", " ” ");
			line = line.replaceAll("؟؟", "?");
			line = line.replaceAll("!!", "! !");
			line = line.replaceAll("!!!", " !!!");
			line = line.replaceAll("،", " , ");
			line = line.replaceAll(",", " , ");
			line = line.replaceAll("«", "\" ");
			line = line.replaceAll("»", " \"");
			line = line.replaceAll("\\(", "( ");
			line = line.replaceAll("\\( \\(", "((");
			line = line.replaceAll("\\)", " )");
			line = line.replaceAll("/", " / ");
			line = line.replaceAll("-", " - ");
			line = line.replaceAll("^", " ^ ");
			line = line.replaceAll("_", " _ ");
			line = line.replaceAll("\\*", " * ");
			line = line.replaceAll(":", " : ");
			line = line.replaceAll("٪", " % ");
			line = line.replaceAll("؛", " ; ");
			line = line.replaceAll("\"", " \" ");
			line = line.replaceAll(" +", " ");	//fix duplicate spaces
			
			if(line.contains(".وحمد"))
				line = line.replaceAll("\\.وحمد", ". وحمد");

			//Match @@ to original
			StringTokenizer tok = new StringTokenizer(line);
			StringTokenizer madatok = new StringTokenizer(madaline);
			//System.out.println(linenum + " mada: " + madaline + "\norig: " + line);
			while(madatok.hasMoreTokens()){
				String madaword = madatok.nextToken();
				//System.out.print("madaword: " + madaword);
				//if(madaword.equals(",") || madaword.equals("\"") || madaword.equals("-"))
				//	newline += madaword + " ";
				if(madaword.contains("@")){
				    try{
					String w = tok.nextToken();
					//System.out.println(" match: " + w);
					newline += w + " ";
				    }
				    catch(NoSuchElementException nsee){
					System.out.println("NoSuchElementException:");
					System.out.println(linenum + " line: " + line);
					System.out.println("madaline: " + madaline);
					System.out.println("newline: " + newline);
					//outfile.close();
					//infile.close();
					//madafile.close();
					//System.exit(1);
				    }
				}
				else{
					if((madaword.charAt(madaword.length()-1) == '+') 
						|| (madaword.charAt(0) == '+')){	//skip past clitics
						newline += madaword + " ";
						//System.out.println(" (skipped clitic)");
					}
					else{
						if(tok.hasMoreTokens()){
							String wo = tok.nextToken();		//match base word
							//System.out.println(" match: " + wo + " (used mada)");
						}
						newline += madaword + " ";
					}
				}
			}//end while

			//write sentence to outfile
			outfile.write(newline.trim() + "\n");
			linenum++;
		}//end while hasNextLine

		infile.close();
		madafile.close();
		outfile.close();
	}
	catch(IOException e){
		System.out.println(e.getMessage());
	}
}//end main

public static char unbuckwalter(char c){
	if((c == '@') || (c == '+'))
		return c;
	else if(c == 'A')
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

}
















