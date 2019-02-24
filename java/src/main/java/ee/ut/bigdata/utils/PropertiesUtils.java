package ee.ut.bigdata.utils;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Properties;

public class PropertiesUtils {

	public static File store(Properties props, String name) {
		File file = new File(name + ".properties");
		try (OutputStream output = new FileOutputStream(file)) {
			props.store(output, null);
			return file;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}
}
