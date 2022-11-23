package test;

import java.io.*;
import java.nio.file.*;
import java.util.Arrays;
public class copydir {
	public static void main(String[] args){
		File file = new File("D:\\Test");
		File[] fs = file.listFiles();
		
		Arrays.sort(fs);
		
		File newdir = new File(file.getAbsolutePath() + "\\Renamed");
		if(!newdir.exists()) newdir.mkdir();
		
		for(int i = 0; i < fs.length; i++) {
			if(fs[i].isDirectory())continue;
			try {
				Path oldfile = fs[i].toPath();
				String filename = fs[i].toString();
				String ext = filename.substring(filename.lastIndexOf(".") + 1);
				
				Path newfile = Paths.get(oldfile.getParent() + "\\Renamed\\LHD_"+(i+1)+"." + ext);
				
				Files.copy(oldfile, newfile ,  StandardCopyOption.REPLACE_EXISTING);
			}
			catch(IOException e ) {
				e.printStackTrace();
			}
		}
		
	}
}
