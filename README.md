# Gram-negative activity as a permeability proxy

Gram-negative and gram-positive MIC data from CoADD was used to train a Chemprop model that predicts activity against Escherichia coli (gram-negative) with respect to Staphylococcus aureus (gram-positive). Active compounds in both pathogens were labeled as permeable, whereas inactive compounds in gram-negative but active in gram-positive were labeled as impermeable.

This model was incorporated on 2025-12-10.


## Information
### Identifiers
- **Ersilia Identifier:** `eos9x3z`
- **Slug:** `gram-negative-permeability-proxy`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Antimicrobial resistance`
- **Target Organism:** `Escherichia coli`, `Staphylococcus aureus`
- **Tags:** `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher likelihood of permeability gram-negative activity, understood as a proxy for permeability.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| gn_activity | float | high | Probability of gram-negative acivity as a proxy for permeability |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9x3z.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9x3z.zip)

### Resource Consumption
- **Model Size (Mb):** `240`
- **Environment Size (Mb):** `6124`


### References
- **Source Code**: [https://pubs.acs.org/doi/suppl/10.1021/acs.jmedchem.1c01984/suppl_file/jm1c01984_si_001.zip](https://pubs.acs.org/doi/suppl/10.1021/acs.jmedchem.1c01984/suppl_file/jm1c01984_si_001.zip)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01984](https://pubs.acs.org/doi/10.1021/acs.jmedchem.1c01984)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9x3z
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9x3z
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
