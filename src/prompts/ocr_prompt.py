def get_input_prompt(json_format):
    return f"""Bạn là một chuyên viên phân tích tài chính. Hãy đọc file PDF báo cáo tài chính này và trích xuất dữ liệu từ các Bảng Cân đối kế toán, Báo cáo Kết quả kinh doanh, và Báo cáo Lưu chuyển tiền tệ.

QUAN TRỌNG - Xử lý số liệu:
1. Định dạng số Việt Nam: dấu chấm (.) là phân cách hàng nghìn (VD: 35.503.251)
2. Bỏ tất cả dấu chấm phân cách và chỉ lấy con số gốc
3. Số trong ngoặc đơn () là số âm
4. Trả về giá trị số nguyên không có dấu phân cách

Ví dụ chuyển đổi:
- "35.503.251" → 35503251
- "(1.234.567)" → -1234567
- "12.500" → 12500

Định dạng đầu ra phải là JSON tuân thủ nghiêm ngặt theo cấu trúc: {json_format}

Nếu một mục không có dữ liệu, hãy để giá trị là 0."""


def get_model_prompt():
    return """**Identifying Key Financial Data**

I'm currently focused on extracting the essential financial statements: the Balance Sheet, Income Statement, and Cash Flow Statement. My strategy involves pinpointing the location of these statements within the PDF document. Once identified, I'll hone in on the specific line items and corresponding values for the year mentioned in the PDF, ensuring accuracy in my data extraction.


**Locating Specific Statement Items**

I've moved on to the intricate process of mapping the provided `field_code` structure to the actual Vietnamese financial report. I'm encountering a challenge: the provided JSON data structure may not perfectly align with every company's financial statements. Therefore, I'm adapting my approach to accurately locate and extract relevant line items from the company's actual report.


**Revising Statement Item Mapping**

I'm now revising my mapping strategy to accommodate the unique structure of the company's financial statements. Since the initial `field_code` structure may be designed for a different company, I'm analyzing the actual report structure. I'm focusing on key financial items, identifying related assets, liabilities, and equity items. I'm also carefully noting the key Vietnamese labels found within the financial statements to craft an accurate extraction strategy. I'm focusing on the main items for the year mentioned in the PDF.


**Pinpointing Key Financial Elements**

I've outlined my plan to locate and extract data. I'm focusing on identifying the Balance Sheet, Income Statement, and Cash Flow Statement within the PDF. I'll then pinpoint the year mentioned in the PDF financial data using the column labels. I'm comparing the provided sample JSON `field_code` structure to the actual structure of the company's financial statements for accuracy. I'm carefully examining the page layout and Vietnamese labels to determine where to find key financial items.


**Extracting and Mapping Line Items**

I'm now focusing on mapping the company's Balance Sheet (Bảng Cân Đối Kế Toán) line items to the provided `field_code` structure. I'm carefully analyzing the actual report, identifying corresponding Vietnamese labels. Given the structure may be tailored to a different company, I'll adapt my strategy to create new `field_code` mappings for items not present in the original structure. I'll accurately extract data from all relevant financial statement items.


**Adapting Extraction for Company Data**

I'm now focusing on the nuances of extracting data from the company's financial statements. Since the given JSON structure may be tailored to a different company, I'm adapting to identify company-specific labels and items within the financial statements and mapping them to appropriate `field_code` structures. My primary target is the financial data from year mention in the PDF. I'll meticulously map the provided `field_codes` to their corresponding Vietnamese labels.


**Identifying Company's Financial Items**

I'm now focusing on the company's financial statements. Since the example JSON structure may be tailored for a different company, I'm identifying corresponding line items within the company's PDF, mapping relevant financial items to respective field codes for accurate extraction. This phase involves a careful review of the company's year mention in the PDF financial data.


**Identifying Report Data Extraction Strategy**

I've detailed my plan to process the PDF. First, I'm identifying key statements: the Balance Sheet, Income Statement, and Cash Flow Statement. Next, I'll pinpoint the year year mention in the PDF data, which I will then extract, format, and prepare for structured output. My approach involves thorough analysis of the PDF's layout, paying close attention to both Vietnamese labels and English column headers to pinpoint the financial information for year mention in the PDF.


**Extracting Company-Specific Financial Data**

I'm now adapting my extraction process to align with the company's financial statements. The JSON's expected structure may necessitate creating several new field codes to accommodate the company's unique line items. Using the example format, I'm carefully extracting and matching Vietnamese descriptions to `field_code`s for accuracy, while also building new `field_code`s if the examples provided do not match.


**Mapping Financial Statements Data**

I'm making excellent progress in mapping the company's financial statements to the required JSON format. I've successfully identified the financial statement items and assigned new `field_codes` where necessary for an accurate extraction of data. The data conversion, such as removing dots and handling negative values, is going smoothly.


**Extracting Financial Statement Data**

I've made substantial progress in extracting the key financial data from the company's PDF. I'm focusing on the Balance Sheet, Income Statement, and Cash Flow Statement, mapping items to appropriate `field_code`s. I'm also paying close attention to formatting rules like removing dots and handling negative values. My goal is to extract the year mention in the PDF financial data as accurately as possible.


**Initiating Data Mapping Process**

I've started the mapping process by carefully reviewing the financial statements' Vietnamese labels. I'm focusing on key financial items and their corresponding year mention in the PDF values. I'm identifying the equivalent JSON field codes, building new ones where the company-specific items don't align. The aim is a comprehensive mapping for accurate data extraction.


**Analyzing Financial Statement Structure**

I'm now deep into mapping the financial statement items from the company's report to the necessary JSON structure. The provided example JSON and `field_code`s, intended for a reference company, are a starting point. I'm focusing on key financial statement items and assigning appropriate field codes. I will create new `field_code`s if the examples do not suffice. I'm focused on extracting the year mention in the PDF financial data.


**Extracting Company-Specific Financial Data**

I've been meticulously comparing the provided JSON structure against the company's year mention in the PDF financial reports, focusing on all financial statements. I'm extracting and building new `field_code`s for specific items as needed. I'm also ensuring the correct extraction and format of values. I'm creating a specific structure tailored to the company's needs.


**Adapting Data for Company**

I've made substantial progress in extracting and structuring the year mention in the PDF financial data for the company. I've meticulously reviewed the Balance Sheet, Income Statement, and Cash Flow Statement. I've mapped the Vietnamese labels to corresponding `field_code`s and created new ones where needed. I'm focusing on cleaning the data by removing the dots and ensuring that parentheses are correctly converted to negative values. The output will reflect the data in the required format.


**Adapting Data Mapping for Company**

I'm now implementing the plan by creating field codes based on the provided JSON's structure and the extracted data. Given the provided JSON's structure and the financial statements, I'm mapping Vietnamese labels to `field_code`s and building new ones as needed. The ultimate aim is to create structured JSON data from the company's year mention in the PDF financial statements and align with the intended data extraction.


**Mapping Company's Financials**

I'm now integrating the extracted financial data for the company into a structured JSON format. I'm carefully mapping Vietnamese labels to relevant field codes, creating new ones as necessary. Data cleanup, including the removal of dots and the correct handling of parentheses for negative values, is underway. I'm focusing on ensuring accuracy in data mapping for the Balance Sheet, Income Statement, and Cash Flow Statement from the year mention in the PDF financial report.


**Extracting and Formatting Financial Data**

I'm now in the final phase, integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I'm making sure all the values, including those from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. For instance, I'm now converting parentheses to represent negative values. I'll make sure all the data conforms to the expected structure.


**Adapting Data Mapping for Company**

I'm now integrating the extracted and formatted data from the company's financial statements into the desired JSON structure. I'm carefully assigning appropriate field codes, ensuring a clear and organized representation. I'm also addressing value cleaning, like eliminating dots and correctly interpreting parentheses to represent negative numbers. The conversion is going smoothly, and I'm close to a final, well-structured output.


**Refining Data Extraction for JSON**

I'm now integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I'm making sure all the values, including those from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. For instance, I'm now converting parentheses to represent negative values. I'll make sure all the data conforms to the expected structure.


**Reconciling Data Extraction**

I've re-evaluated my approach to ensure strict adherence to the provided `field_code` structure. I'm focusing on fitting the extracted data from the company's Balance Sheet, Income Statement, and Cash Flow Statement into the existing `field_code`s. I'm making sure all line items are accounted for and mapping them to the closest `field_code` for the complete JSON structure. I will extract the values and assign 0 to any line items missing from the financial statements.


**Aligning Data Extraction**

I'm now integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I'm making sure all the values, including those from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. For instance, I'm now converting parentheses to represent negative values. I'll make sure all the data conforms to the expected structure.


**Adapting Data for Final JSON**

I'm now integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I've made sure all the values, from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. I've converted parentheses to negative values to ensure data integrity. I'll make sure the JSON structure is accurate and consistent.


**Analyzing Field Mapping Strategy**

I'm finalizing the data integration and mapping for the company's financial statements to align with the provided `field_code` structure, using year mention in the PDF data. I am setting the unmapped fields to 0, ensuring accuracy in line-item mapping from the financial statements. I will complete this process for all financial statements, meticulously following the instruction to build a clean JSON with the given `field_code` structure. I will prioritize filling in with the actual data from year mention in the PDF.


**Analyzing Data Extraction Strategy**

I'm methodically mapping the company's financial data to the example JSON structure, meticulously assigning existing `field_code`s or establishing new ones for accurate year mention in the PDF financial data representation. I'm evaluating the financial statement elements for suitable `field_code` counterparts. I am checking the line items for accurate mapping.


**Analyzing Value Extraction Strategy**

I'm now integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I'm making sure all the values, including those from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. For instance, I'm now converting parentheses to represent negative values. I'll make sure all the data conforms to the expected structure.


**Analyzing Field Code Mapping**

I'm now fully immersed in aligning the company's financial data to the `field_code` structure, using year mention in the PDF data, based on the provided field codes. I am prioritizing the extraction and mapping, understanding the given codes may not always perfectly fit every company's unique line items.


**Analyzing Financial Statement Items**

I'm now fully immersed in aligning the company's data with the example JSON structure and field codes. While the example structure is generic, I'm making sure all values are mapped from the year mention in the PDF financial statements. I will map line items to closest-matching `field_code`s and assign 0 to items not found, while constructing an accurate JSON output.


**Reconciling Company Financial Data**

I've meticulously crafted a JSON structure by mapping line items from the company's balance sheet, income statement, and cash flow statement to the predefined `field_code` structure. I'm focusing on financial data for year mention in the PDF, setting unmatched values to 0 and mapping items with a focus on line item data accuracy.


**Analyzing Final Data Integration**

I'm now integrating the extracted data into a JSON structure, carefully mapping fields to their corresponding `field_code`. I've made sure all the values, including those from the Balance Sheet, Income Statement, and Cash Flow Statement, are accurately represented within the prescribed format for the year year mention in the PDF. I'll make sure the JSON structure is accurate and consistent."""