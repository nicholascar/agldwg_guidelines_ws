from flask import Blueprint, Response, request, redirect, render_template, send_from_directory
routes = Blueprint('routes', __name__)
import os
import functions
import settings
import markdown


#
#   All the routes in the API
#
@routes.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(routes.root_path, 'static/img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@routes.route('/')
def home():
    return render_template('page_index.html')


@routes.route('/contact')
def contact():
    return render_template('page_contact.html')


@routes.route('/rule/<string:rule_id>')
def rule(rule_id):
    from data import rules

    if request.args.get('_property') == 'definition':
        txt = rules.rules[rule_id]['text'].decode('utf-8')
        if request.args.get('_format') == 'text/plain':
            return Response(txt, status=200, mimetype='text/plain')
        else:  # HTML (text/html) is default
            html = markdown.markdown(txt)
            return Response(html, status=200, mimetype='text/html')

    elif request.args.get('_property') == 'directive':
        txt = rules.rules[rule_id]['directive'].decode('utf-8')
        if request.args.get('_format') == 'text/plain':
            return Response(txt, status=200, mimetype='text/plain')
        else:  # HTML (text/html) is default
            html = markdown.markdown(txt)
            return Response(html, status=200, mimetype='text/html')

    elif request.args.get('_property') == 'code':
        return Response(rules.rules[rule_id]['code'], status=200, mimetype='text/plain')

    else:  # landing & alternates
        return render_template('page_rule.html',
                               rule=rules.rules[rule_id])

    #return render_template('page_rules.html')


@routes.route('/example')
def example_resource():
    import json

    if ('text/turtlez' in request.headers['accept'] or
        request.args.get('_format') == 'text/turtle'):
        resp = '''@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix ba: <http://data.bioregionalassessments.gov.au/def/ba#> .
@prefix : <https://data.bioregionalassessments.gov.au/datastore/dataset/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .

:15fc009f-7b7c-46e2-9ebe-57d7e840d692 a prov:Entity ;
    ba:dataOwner <http://data.bioregionalassessments.gov.au/id/person/veronika.galinec.9> ;
    ba:data_path "/SYD/HUN/DATA/Geography/Topography/Cartography/"^^xsd:string ;
    ba:folder_name "Hun_label_mask"^^xsd:string ;
    ba:write_status "locked"^^xsd:string ;
    dc:created "2015-03-03T04:52:11"^^xsd:dateTime ;
    dc:title "HUN_label_mask"
.
'''
        return Response(resp, status=200, mimetype='text/turtle')

    elif ('application/ld+jsonz' in request.headers['accept'] or
          request.args.get('_format') == 'application/ld+json'):
        resp = [{
            "@id": "https://data.bioregionalassessments.gov.au/datastore/dataset/15fc009f-7b7c-46e2-9ebe-57d7e840d692",
            "@type": [
                "http://www.w3.org/ns/prov#Entity"
            ],
            "http://data.bioregionalassessments.gov.au/def/ba#dataOwner": [
                {
                    "@id": "http://data.bioregionalassessments.gov.au/id/person/veronika.galinec.9"
                }
            ],
            "http://data.bioregionalassessments.gov.au/def/ba#data_path": [
                {
                    "@value": "/SYD/HUN/DATA/Geography/Topography/Cartography/"
                }
            ],
            "http://data.bioregionalassessments.gov.au/def/ba#folder_name": [
                {
                    "@value": "Hun_label_mask"
                }
            ],
            "http://data.bioregionalassessments.gov.au/def/ba#write_status": [
                {
                    "@value": "locked"
                }
            ],
            "http://purl.org/dc/elements/1.1/created": [
                {
                    "@type": "http://www.w3.org/2001/XMLSchema#dateTime",
                    "@value": "2015-03-03T14:52:11+00:00"
                }
            ],
            "http://purl.org/dc/elements/1.1/title": [
                {
                    "@value": "HUN_label_mask"
                }
            ]
        }]

        return Response(json.dumps(resp), status=200, mimetype='application/json')

    elif ('application/rdf+xmlz' in request.headers['accept'] or
          request.args.get('_format') == 'application/rdf+xml'):
        resp = '''
<rdf:RDF
   xmlns:ns1="http://purl.org/dc/elements/1.1/"
   xmlns:ns2="http://data.bioregionalassessments.gov.au/def/ba#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
  <rdf:Description rdf:about="https://data.bioregionalassessments.gov.au/datastore/dataset/15fc009f-7b7c-46e2-9ebe-57d7e840d692">
    <ns2:dataOwner rdf:resource="http://data.bioregionalassessments.gov.au/id/person/veronika.galinec.9"/>
    <rdf:type rdf:resource="http://www.w3.org/ns/prov#Entity"/>
    <ns1:created rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2015-03-03T04:52:11</ns1:created>
    <ns2:data_path rdf:datatype="http://www.w3.org/2001/XMLSchema#string">/SYD/HUN/DATA/Geography/Topography/Cartography/</ns2:data_path>
    <ns2:folder_name rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Hun_label_mask</ns2:folder_name>
    <ns1:title>HUN_label_mask</ns1:title>
    <ns2:write_status rdf:datatype="http://www.w3.org/2001/XMLSchema#string">locked</ns2:write_status>
  </rdf:Description>
</rdf:RDF>
'''
        return Response(resp, status=200, mimetype='application/rdf+xml')

    else:  # HTML
        resp = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>A Dataset</title>
        </head>
        <body>
            <h1>A Dataset</h1>
            <table class="tbl_views">
                <tr><th>Title</th><td>HUN_label_mask</td></tr>
                <tr>
                    <th>ID<br />URI</th>
                    <td>15fc009f-7b7c-46e2-9ebe-57d7e840d692<br /><a href="https://data.bioregionalassessments.gov.au/datastore/dataset/15fc009f-7b7c-46e2-9ebe-57d7e840d692">https://data.bioregionalassessments.gov.au/datastore/dataset/15fc009f-7b7c-46e2-9ebe-57d7e840d692</a></td>
                </tr>
                    <tr>
                        <th>Metadata</th>
                        <td><a href="http://badms.csiro.au/Home/Search?datasetMetadataId=15fc009f-7b7c-46e2-9ebe-57d7e840d692">Go to Metadata Catalogue entry</a></td>
                    </tr>
                    <tr>
                        <th>Data path</th>
                        <td>SYD/HUN/DATA/Geography/Topography/Cartography/Hun_label_mask</td>
                    </tr>
                    <tr>
                        <th>Status</th>
                        <td>locked</td>
                    </tr>

                    <tr>
                        <th>Formats</th>
                        <td>
                             <a href="/example?_format=text/turtle">Turtle</a> |
                            <a href="/example?_format=application/rdf%2Bxml">RDF/XML</a> |
                            <a href="/example?_format=application/ld%2Bjson">JSON</a>
                        </td>
                    </tr>
                    <tr>
                        <th style="vertical-align:top;">Contents</th>
                        <td><div id="fileTree" class="demo"></div></td>
                    </tr>
            </table>
        </body>
        </html>
'''
        return Response(resp, status=200, mimetype='text/html')


@routes.route('/example2')
def example_redirect():
    return redirect('http://google.com', code=303)