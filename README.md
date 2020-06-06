# Pygments Tool

There is a library for python called [pygments](https://pygments.org/). The library takes a source code file and then renders an image/svg/etc of what the code would look like using presets that people commonly use.

Needless to say the presets that come with the CLI utility did not have the themes that I prefer such as AyuMirage and OneDark. So I wrote a tool to use either of them.


Here is what the input file (`/docs/Variables.java`) looks like:
```java
class Variables {
	public static void main(String[] args) {
		String name = "Ken";
		int age = 2;
	}
}
```

Here is what the output looks like in the One Dark Style (SVG file):

![Output of the Variables.java file](docs/output.svg)