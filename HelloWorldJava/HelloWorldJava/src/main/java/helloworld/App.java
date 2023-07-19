package helloworld;


import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<String, String> {

    public String handleRequest(String input, Context context) {
        context.getLogger().log("Input: " + input);
        return "Hello World";
    }
}
