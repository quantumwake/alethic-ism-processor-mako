# Alethic Instruction-Based State Machine (Mako Processor)

A component of the Alethic ISM framework that executes Mako templates. This processor allows for input streams and events to process inbound messages using Mako template rendering and produce output streams and/or events.

## Overview

The Mako Processor:
- Renders Mako templates with input data
- Processes input items through user-defined Mako templates
- Supports both batch processing and streaming operations
- Provides template-based data transformation capabilities
- Integrates with the broader ISM messaging system

## Usage

To use the Mako Processor, you create a Mako template that defines how your input data should be rendered. The template receives a context with the input data under the `items` key:

```mako
## Mako template to process input data
<%
    import json
%>
% for query in items:
    ${json.dumps(query)}
% endfor
```

## Examples

### Example 1: Basic Data Processing

This example demonstrates processing input items and formatting the output:

```mako
<%
    import json
%>
% for i, query in enumerate(items):
    Query ${i + 1}: ${json.dumps(query, indent=2)}
% endfor
```

### Example 2: JSON Output Generation

This example shows how to generate JSON output from input items:

```mako
<%
    import json
    
    # Process all items and create output
    output = []
    for query in items:
        result = {
            'processed': True,
            'original_data': query
        }
        output.append(result)
%>
${json.dumps(output, indent=2)}
```

### Example 3: HTML Table Generation

A simple example that generates an HTML table from input items:

```mako
<table>
    <thead>
        <tr>
            <th>Index</th>
            <th>Data</th>
        </tr>
    </thead>
    <tbody>
% for i, query in enumerate(items):
        <tr>
            <td>${i + 1}</td>
            <td>${query}</td>
        </tr>
% endfor
    </tbody>
</table>
```

### Example 4: Complex Data Transformation

This example demonstrates a more complex Mako template with data transformation:

```mako
<%
    import json
    from datetime import datetime
    
    # Transform items
    transformed_data = []
    for query in items:
        item = {
            'timestamp': datetime.now().isoformat(),
            'query_id': query.get('id', 'unknown'),
            'data': query,
            'status': 'processed'
        }
        transformed_data.append(item)
%>
## Processed Results

% for item in transformed_data:
- Query ID: ${item['query_id']}
  Timestamp: ${item['timestamp']}
  Status: ${item['status']}
  Data: ${json.dumps(item['data'], indent=4)}

% endfor
```

## Template Processing

The Mako Processor uses the Mako templating engine to transform input data:


- *Templates receive input data in the `items` context variable (if the input values is a list of dictionaries)
- *Templates receive input data in the context variable (if the input values is a dictionary)
- Full Mako expressions are available within template blocks
- Output is generated through template rendering
- Templates can generate any text-based format (JSON, HTML, XML, etc.)
- The `build_template_text_v2` utility function handles the template rendering

Mako templates provide a safe and flexible way to transform data within the ISM framework.
