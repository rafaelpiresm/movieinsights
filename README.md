<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>feedback-loop-udfs</groupId>
	<artifactId>feedback-loop-udfs</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<properties>
		<downloadSources>true</downloadSources>
		<downloadJavadocs>true</downloadJavadocs>
	</properties>
	<build>

		<plugins>

			<plugin>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.6.0</version>
				<configuration>
					<source>1.8</source>
					<target>1.8</target>
				</configuration>
			</plugin>

			<plugin>
				<groupId>net.alchim31.maven</groupId>
				<artifactId>scala-maven-plugin</artifactId>
				<version>3.4.6</version>
				<executions>
					<execution>
						<id>scala-compile-first</id>
						<phase>process-resources</phase>
						<goals>
							<goal>add-source</goal>
							<goal>compile</goal>
						</goals>
					</execution>
					<execution>
						<id>scala-test-compile</id>
						<phase>process-test-resources</phase>
						<goals>
							<goal>testCompile</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
			<plugin>
				<!-- NOTE: We don't need a groupId specification because the group is 
					org.apache.maven.plugins ...which is assumed by default. -->
				<artifactId>maven-assembly-plugin</artifactId>
				<version>3.1.0</version>
				<configuration>
					<descriptorRefs>
						<descriptorRef>jar-with-dependencies</descriptorRef>
					</descriptorRefs>
					<archive>
						<manifest>
							<mainClass>br.com.bradesco.ingestao.App</mainClass>
						</manifest>
					</archive>
				</configuration>
				<executions>
					<execution>
						<id>assemble-all</id>
						<phase>package</phase>
						<goals>
							<goal>single</goal>
						</goals>
					</execution>
				</executions>
			</plugin>
		</plugins>
	</build>
	<dependencies>
		<!-- https://mvnrepository.com/artifact/junit/junit -->
		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.12</version>
			<scope>test</scope>
		</dependency>
		
		<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-core -->
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-core_2.11</artifactId>
			<version>2.3.3</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.apache.spark/spark-sql -->
		<dependency>
			<groupId>org.apache.spark</groupId>
			<artifactId>spark-sql_2.11</artifactId>
			<version>2.3.3</version>
		</dependency>
		<dependency>
			<groupId>jdk.tools</groupId>
			<artifactId>jdk.tools</artifactId>
			<scope>system</scope>
			<!--<systemPath>C:/Program Files/Java/jdk1.7.0_80/lib/tools.jar</systemPath> -->
			<systemPath>${env.JAVA_HOME}/lib/tools.jar</systemPath>
			<version>1.8</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-hdfs -->
		<dependency>
			<groupId>org.apache.hadoop</groupId>
			<artifactId>hadoop-hdfs</artifactId>
			<version>2.7.0</version>
		</dependency>


	</dependencies>
</project>
