
import java.io.*;
import java.util.*;

public class PostProcess{

public static void main(String[] args){

	if(args.length<3){
		System.out.println("Usage: java PostProcess original.one fomaoutput.one outname");
	}

	try{
		Scanner original = new Scanner(new FileReader(args[0]));
		Scanner foma = new Scanner(new FileReader(args[1]));
		FileWriter out = new FileWriter(args[2]);

		String buffer = "";

		while(original.hasNextLine()){
			//get next original word
			String orig = original.nextLine();
			if(orig.equals("")){
				foma.nextLine();
				foma.nextLine();
				out.write(buffer.trim() + "\n");
				buffer = "";
			}
			else{
				ArrayList<String> options = new ArrayList<String>();
				String w = foma.nextLine();

				//get all foma options
				while(!w.equals("") && foma.hasNextLine()){ 
					options.add(w);
					w = foma.nextLine();
				}

				//process foma options
				if(options.size()==1){
					String f = options.get(0);
					if(f.equals("+?") || f.equals(orig))
						buffer += orig + " ";
					else{
						f = f.replaceAll("\\+", " ");
						buffer += f + " ";
					}
				}//end if only 1 option
				else{
					//if only one true analysis, use that
					int numplus = 0;
					String bestopt = options.get(0);
					for(String opt : options){
						if(opt.contains("+")){
							numplus++;
							bestopt = opt;
						}
					}//end for
					if(numplus==1){
						bestopt = bestopt.replaceAll("\\+", " ");
						buffer += bestopt + " ";
					}
					else{	//TODO:pick best option
						//bestopt = options.get(0);

						Random rand = new Random(System.currentTimeMillis());
						int in = rand.nextInt(options.size());
						bestopt = options.get(in);

						bestopt = bestopt.replaceAll("\\+", " ");
						buffer += bestopt + " ";
					}
				}//end multiple options
			}//end else
		}//end while

		if(!buffer.equals(""))
			out.write(buffer.trim() + "\n");

		original.close();
		foma.close();
		out.close();

	}//end try
	catch(IOException e){
		System.out.println(e.getMessage());
	}

}//end main

}
