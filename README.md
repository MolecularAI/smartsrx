# Repository of the `smartsrx`

The home of the `SMARTS-RX` project.

## Authors and Collaborators (alphabetically)
- Eike Caldeweyher (A-DMTA)
- Mikhail Kabeshov (MAI)
- Thierry Kogej (MAI)

## Maintainers (alphabetically)
- Christos Kannas (MAI)

## Setting Up the Python Environment

To use the provided code for updating `smartsrx`, follow these steps to set up the Python environment:

### Prerequisites
Ensure you have the following installed:
- Python 3.9 or later (recommended version: 3.10)
- `poetry` 2.1.3 (Python package manager)

***Note:** You can either create this base environment manually or create a `conda` environment with `smartsrx-env.yml`.*

### Steps to Set Up
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MolecularAI/smartsrx.git
   cd smartsrx
   ```
2.  **Install Dependencies**:
    ```bash
    poetry install
    ```
3. **Verify Installation**:
    ```bash
    python -m pip list --format=freeze
    ```

### Generate `smartsrx.json`:
1. Update `SMARTS_RX.txt`
2. Run the script:
   ```bash
   python -m smartsrx.create_json
   ```

### Update the README Table:
1. After updating `SMARTS_RX.txt` and generating the JSON file:
2. Run the table update script:
   ```bash
   python -m smartsrx.update_readme_table
   ```
   This will automatically extract class, subclass, and `SMARTS-RX` information from the `SMARTS_RX.txt` file and update the table below.

## Obtain `smartsrx` via RDKit

We obtain `smartsrx` by loading the SMARTS library into an RDKit `FilterCatalog`.
Each SMARTS is added as a *SmartsMatcher* entry.
We create an RDKit molecule for the molecule of interest and use the `GetMatches` method of the `FilterCatalog` instance.
We obtain the unique identifiers through the `GetDescription` method of each match, and concatenate the strings.
The final concatenated string is our `SMARTS-RX` identifier.

## `SMARTS-RX` documentation

Extended `SMARTS-RX` documentation can be found as Word documents in [docs](./docs/) folder.

## Classes and Subclasses

Classes and subclasses are defined in the original data file, which is versionised to match the `smartsrx` version.

Below we list classes and subclasses for the current `smartsrx` version (v1.0.0):
<!-- The table will be populated by the update_readme_table.py script -->

| Class | Subclass | `SMARTS-RX` |
|:------:|:--------:|:----------:|
| Thioacid | Thioacid_Aliphatic | Thioacid_SaturatedAliphatic |
| Thioacid | Thioacid_Aliphatic | Thioacid_UnsaturatedAliphatic |
| Thioacid | Thioacid_Aromatic | Thioacid_Aromatic |
| Thioacid | Thioacid_Heteroaromatic | Thioacid_Heteroaromatic |
| Acid | Acid_Aliphatic | Acid_SaturatedAliphatic |
| Acid | Acid_Aliphatic | Acid_UnsaturatedAliphatic |
| Acid | Acid_Aromatic | Acid_Aromatic |
| Acid | Acid_Heteroaromatic | Acid_Heteroaromatic |
| Acid | Acid_Carbamic | Acid_Carbamic |
| Thioacid | Thioacid_Carbamic | Thioacid_Carbamic |
| Acid | Acid_Carbonic | Acid_Carbonic |
| Thioacid | Thioacid_Carbonic | Thioacid_Carbonic |
| Acid | Acid_Thiocarbonic | Acid_Thiocarbonic |
| Thioacid | Thioacid_Thiocarbonic | Thioacid_Thiocarbonic |
| AcidX | Xformamide | Xformamide |
| AcidX | XThioformate | XThioformate |
| AcidX | XFormate | XFormate |
| AcidX | AcidX_Aliphatic | AcidX-Fluoride_SaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Chloride_SaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Bromide_SaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Iodide_SaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Triflate_SaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Fluoride_UnsaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Chloride_UnsaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Bromide_UnsaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Iodide_UnsaturatedAliphatic |
| AcidX | AcidX_Aliphatic | AcidX-Triflate_UnsaturatedAliphatic |
| AcidX | AcidX_Aromatic | AcidX-Fluoride_Aromatic |
| AcidX | AcidX_Aromatic | AcidX-Chloride_Aromatic |
| AcidX | AcidX_Aromatic | AcidX-Bromide_Aromatic |
| AcidX | AcidX_Aromatic | AcidX-Iodide_Aromatic |
| AcidX | AcidX_Aromatic | AcidX-Triflate_Aromatic |
| AcidX | AcidX_Heteroaromatic | AcidX-Fluoride_Heteroaromatic |
| AcidX | AcidX_Heteroaromatic | AcidX-Chloride_Heteroaromatic |
| AcidX | AcidX_Heteroaromatic | AcidX-Bromide_Heteroaromatic |
| AcidX | AcidX_Heteroaromatic | AcidX-Iodide_Heteroaromatic |
| AcidX | AcidX_Heteroaromatic | AcidX-Triflate_Heteroaromatic |
| Anhydride | Anhydride | Anhydride |
| XKetone | XKetoneAromaticFluoride | XKetoneAromaticFluoride |
| XKetone | XKetoneAromaticChloride | XKetoneAromaticChloride |
| XKetone | XKetoneAromaticBromide | XKetoneAromaticBromide |
| XKetone | XKetoneAromaticIodide | XKetoneAromaticIodide |
| XKetone | XKetoneAromaticTriflate | XKetoneAromaticTriflate |
| XKetone | XKetoneAliphaticFluoride | XKetoneAliphaticFluoride |
| XKetone | XKetoneAliphaticChloride | XKetoneAliphaticChloride |
| XKetone | XKetoneAliphaticBromide | XKetoneAliphaticBromide |
| XKetone | XKetoneAliphaticIodide | XKetoneAliphaticIodide |
| XKetone | XKetoneAliphaticTriflate | XKetoneAliphaticTriflate |
| Bocanhydrate | Bocanhydrate | Bocanhydrate |
| Mesylate | Mesylate | Mesylate |
| Mesylate | DiMesylate | DiMesylate |
| XF | X_Aliphatic | X-Fluoride_Aliph |
| X | X_Aliphatic | X-Chloride_Aliph |
| X | X_Aliphatic | X-Bromide_Aliph |
| X | X_Aliphatic | X-Iodide_Aliph |
| X | X_Aliphatic | X-Triflate_Aliph |
| XF | X_Aliphatic | X-Fluoride_Vinyl |
| X | X_Aliphatic | X-Chloride_Vinyl |
| X | X_Aliphatic | X-Bromide_Vinyl |
| X | X_Aliphatic | X-Iodide_Vinyl |
| X | X_Aliphatic | X-Triflate_Vinyl |
| XF | X_Aliphatic | X-Fluoride_Alkyne |
| X | X_Aliphatic | X-Chloride_Alkyne |
| X | X_Aliphatic | X-Bromide_Alkyne |
| X | X_Aliphatic | X-Iodide_Alkyne |
| X | X_Aliphatic | X-Triflate_Alkyne |
| XF | X_Aliphatic | X-Fluoride_Nitrile |
| X | X_Aliphatic | X-Chloride_Nitrile |
| X | X_Aliphatic | X-Bromide_Nitrile |
| X | X_Aliphatic | X-Iodide_Nitrile |
| X | X_Aliphatic | X-Triflate_Nitrile |
| XF | X_Fluoride_Aromatic | X-Fluoride_Phe |
| X | X_Aromatic | X-Chloride_Phe |
| X | X_Aromatic | X-Bromide_Phe |
| X | X_Aromatic | X-Iodide_Phe |
| X | X_Aromatic | X-Triflate_Phe |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het6 |
| X | X_Heteroaromatic | X-Chloride_Het6 |
| X | X_Heteroaromatic | X-Bromide_Het6 |
| X | X_Heteroaromatic | X-Iodide_Het6 |
| X | X_Heteroaromatic | X-Triflate_Het6 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het5 |
| X | X_Heteroaromatic | X-Chloride_Het5 |
| X | X_Heteroaromatic | X-Bromide_Het5 |
| X | X_Heteroaromatic | X-Iodide_Het5 |
| X | X_Heteroaromatic | X-Triflate_Het5 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het6Het5 |
| X | X_Heteroaromatic | X-Chloride_Het6Het5 |
| X | X_Heteroaromatic | X-Bromide_Het6Het5 |
| X | X_Heteroaromatic | X-Iodide_Het6Het5 |
| X | X_Heteroaromatic | X-Triflate_Het6Het5 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_PheHet5 |
| X | X_Heteroaromatic | X-Chloride_PheHet5 |
| X | X_Heteroaromatic | X-Bromide_PheHet5 |
| X | X_Heteroaromatic | X-Iodide_PheHet5 |
| X | X_Heteroaromatic | X-Triflate_PheHet5 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het5Het6 |
| X | X_Heteroaromatic | X-Chloride_Het5Het6 |
| X | X_Heteroaromatic | X-Bromide_Het5Het6 |
| X | X_Heteroaromatic | X-Iodide_Het5Het6 |
| X | X_Heteroaromatic | X-Triflate_Het5Het6 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het5Phe |
| X | X_Heteroaromatic | X-Chloride_Het5Phe |
| X | X_Heteroaromatic | X-Bromide_Het5Phe |
| X | X_Heteroaromatic | X-Iodide_Het5Phe |
| X | X_Heteroaromatic | X-Triflate_Het5Phe |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het5Het5 |
| X | X_Heteroaromatic | X-Chloride_Het5Het5 |
| X | X_Heteroaromatic | X-Bromide_Het5Het5 |
| X | X_Heteroaromatic | X-Iodide_Het5Het5 |
| X | X_Heteroaromatic | X-Triflate_Het5Het5 |
| XF | X_Fluoride_Aromatic | X-Fluoride_PhePhe |
| X | X_Aromatic | X-Chloride_PhePhe |
| X | X_Aromatic | X-Bromide_PhePhe |
| X | X_Aromatic | X-Iodide_PhePhe |
| X | X_Aromatic | X-Triflate_PhePhe |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het6Phe |
| X | X_Heteroaromatic | X-Chloride_Het6Phe |
| X | X_Heteroaromatic | X-Bromide_Het6Phe |
| X | X_Heteroaromatic | X-Iodide_Het6Phe |
| X | X_Heteroaromatic | X-Triflate_Het6Phe |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_PheHet6 |
| X | X_Heteroaromatic | X-Chloride_PheHet6 |
| X | X_Heteroaromatic | X-Bromide_PheHet6 |
| X | X_Heteroaromatic | X-Iodide_PheHet6 |
| X | X_Heteroaromatic | X-Triflate_PheHet6 |
| XF | X_Fluoride_Heteroaromatic | X-Fluoride_Het6Het6 |
| X | X_Heteroaromatic | X-Chloride_Het6Het6 |
| X | X_Heteroaromatic | X-Bromide_Het6Het6 |
| X | X_Heteroaromatic | X-Iodide_Het6Het6 |
| X | X_Heteroaromatic | X-Triflate_Het6Het6 |
| Aldehyde | Aldehyde_Aliphatic | Aldehyde_SaturatedAliphatic |
| Aldehyde | Aldehyde_Aliphatic | Aldehyde_UnsaturatedAliphatic |
| Aldehyde | Aldehyde_Aromatic | Aldehyde_Aromatic |
| Aldehyde | Aldehyde_Heteroaromatic | Aldehyde_Heteroaromatic |
| Ketone | KetoneAromaticCyclic | KetoneAromaticCyclic |
| Ketone | KetoneAromaticAcyclic | KetoneAromaticAcyclic |
| Ketone | KetoneAliphaticCyclic | KetoneAliphaticCyclic |
| Ketone | KetoneAliphaticAcyclic | KetoneAliphaticAcyclic |
| Ketone | KetoneMixCyclic | KetoneMixCyclic |
| Ketone | KetoneMixAcyclic | KetoneMixAcyclic |
| Ketone | Thioketone | Thioketone |
| Nitrogen_X | NitrogenFluorideCyclic | NitrogenFluorideCyclic |
| Nitrogen_X | NitrogenFluorideAcyclic | NitrogenFluorideAcyclic |
| Nitrogen_X | NitrogenChlorideCyclic | NitrogenChlorideCyclic |
| Nitrogen_X | NitrogenChlorideAcyclic | NitrogenChlorideAcyclic |
| Nitrogen_X | NitrogenBromideCyclic | NitrogenBromideCyclic |
| Nitrogen_X | NitrogenBromideAcyclic | NitrogenBromideAcyclic |
| Nitrogen_X | NitrogenIodideCyclic | NitrogenIodideCyclic |
| Nitrogen_X | NitrogenIodideAcyclic | NitrogenIodideAcyclic |
| Nitrogen_X | NitrogenTriflateCyclic | NitrogenTriflateCyclic |
| Nitrogen_X | NitrogenTriflateAcyclic | NitrogenTriflateAcyclic |
| Imine | AromaticImine | AromaticImine |
| Imine | AliphaticImine | AliphaticImine |
| Thioester | ThioEsterAcyclic | ThioEsterAcyclic |
| Thioester | ThioEsterCyclic | ThioEsterCyclic |
| Ester | EsterAcyclic | EsterAcyclic |
| Ester | EsterCyclic | EsterCyclic |
| Ester | EsterAromatic | EsterAromatic |
| Nitrile | Nitrile_Aliphatic | Nitrile_SaturatedAliphatic |
| Nitrile | Nitrile_Aliphatic | Nitrile_UnsaturatedAliphatic |
| Nitrile | Nitrile_Aromatic | Nitrile_Aromatic |
| Nitrile | Nitrile_Heteroaromatic | Nitrile_Heteroaromatic |
| Sulfur | Sulfur | Sulfur |
| Sulfonyl | Sulfonyl_Aliphatic | Sulfonyl-Fluoride_Aliphatic |
| Sulfonyl | Sulfonyl_Aliphatic | Sulfonyl-Chloride_Aliphatic |
| Sulfonyl | Sulfonyl_Aliphatic | Sulfonyl-Bromide_Aliphatic |
| Sulfonyl | Sulfonyl_Aliphatic | Sulfonyl-Iodide_Aliphatic |
| Sulfonyl | Sulfonyl_Aliphatic | Sulfonyl-Triflate_Aliphatic |
| Sulfonyl | Sulfonyl_Aromatic | Sulfonyl-Fluoride_Aromatic |
| Sulfonyl | Sulfonyl_Aromatic | Sulfonyl-Chloride_Aromatic |
| Sulfonyl | Sulfonyl_Aromatic | Sulfonyl-Bromide_Aromatic |
| Sulfonyl | Sulfonyl_Aromatic | Sulfonyl-Iodide_Aromatic |
| Sulfonyl | Sulfonyl_Aromatic | Sulfonyl-Triflate_Aromatic |
| Sulfonyl | Sulfonic_Aliphatic | Sulfonic_Aliphatic |
| Sulfonyl | Sulfonic_Aromatic | Sulfonic_Aromatic |
| Sulfinyl | Sulfinyl_Aliphatic | Sulfinyl-Fluoride_Aliphatic |
| Sulfinyl | Sulfinyl_Aliphatic | Sulfinyl-Chloride_Aliphatic |
| Sulfinyl | Sulfinyl_Aliphatic | Sulfinyl-Bromide_Aliphatic |
| Sulfinyl | Sulfinyl_Aliphatic | Sulfinyl-Iodide_Aliphatic |
| Sulfinyl | Sulfinyl_Aliphatic | Sulfinyl-Triflate_Aliphatic |
| Sulfinyl | Sulfinyl_Aromatic | Sulfinyl-Fluoride_Aromatic |
| Sulfinyl | Sulfinyl_Aromatic | Sulfinyl-Chloride_Aromatic |
| Sulfinyl | Sulfinyl_Aromatic | Sulfinyl-Bromide_Aromatic |
| Sulfinyl | Sulfinyl_Aromatic | Sulfinyl-Iodide_Aromatic |
| Sulfinyl | Sulfinyl_Aromatic | Sulfinyl-Triflate_Aromatic |
| SulfonylImine | SulfonylImine_Aliphatic | SulfonylImine-Fluoride_Aliphatic |
| SulfonylImine | SulfonylImine_Aliphatic | SulfonylImine-Chloride_Aliphatic |
| SulfonylImine | SulfonylImine_Aliphatic | SulfonylImine-Bromide_Aliphatic |
| SulfonylImine | SulfonylImine_Aliphatic | SulfonylImine-Iodide_Aliphatic |
| SulfonylImine | SulfonylImine_Aliphatic | SulfonylImine-Triflate_Aliphatic |
| SulfonylImine | SulfonylImine_Aromatic | SulfonylImine-Fluoride_Aromatic |
| SulfonylImine | SulfonylImine_Aromatic | SulfonylImine-Chloride_Aromatic |
| SulfonylImine | SulfonylImine_Aromatic | SulfonylImine-Bromide_Aromatic |
| SulfonylImine | SulfonylImine_Aromatic | SulfonylImine-Iodide_Aromatic |
| SulfonylImine | SulfonylImine_Aromatic | SulfonylImine-Triflate_Aromatic |
| Nitro | Nitro_Aliphatic | Nitro_SaturatedAliphatic |
| Nitro | Nitro_Aliphatic | Nitro_UnsaturatedAliphatic |
| Nitro | Nitro_Aromatic | Nitro_Aromatic |
| Nitro | Nitro_Heteroaromatic | Nitro_Heteroaromatic |
| PFAS | PFAS_Aliphatic | CF2_SaturatedAliphatic |
| PFAS | PFAS_Aliphatic | CF2_UnsaturatedAliphatic |
| PFAS | PFAS_Aromatic | CF2_Aromatic |
| PFAS | PFAS_Heteroaromatic | CF2_Heteroaromatic |
| PFAS | PFAS_Aliphatic | CF3_SaturatedAliphatic |
| PFAS | PFAS_Aliphatic | CF3_UnsaturatedAliphatic |
| PFAS | PFAS_Aromatic | CF3_Aromatic |
| PFAS | PFAS_Heteroaromatic | CF3_Heteroaromatic |
| PFAS | PFAS_Aliphatic | PFAS_SaturatedAliphatic |
| PFAS | PFAS_Aliphatic | PFAS_UnsaturatedAliphatic |
| PFAS | PFAS_Aromatic | PFAS_Aromatic |
| PFAS | PFAS_Heteroaromatic | PFAS_Heteroaromatic |
| Nitroxy | Nitroxy | Nitroxy |
| Diazo | Diazo | Diazo |
| ThioCyanate | ThioCyanate_Aliphatic | ThioCyanate_Aliphatic |
| ThioCyanate | ThioCyanate_Aromatic | ThioCyanate_Aromatic |
| ThioisoCyanate | ThioisoCyanate_Aliphatic | ThioisoCyanate_SaturatedAliphatic |
| ThioisoCyanate | ThioisoCyanate_Aliphatic | ThioisoCyanate_UnsaturatedAliphatic |
| ThioisoCyanate | ThioisoCyanate_Aromatic | ThioisoCyanate_Aromatic |
| ThioisoCyanate | ThioisoCyanate_Heteroaromatic | ThioisoCyanate_Heteroaromatic |
| Cyanate | Cyanate_Aliphatic | Cyanate_Aliphatic |
| Cyanate | Cyanate_Aromatic | Cyanate_Aromatic |
| IsoCyanate | IsoCyanate_Aliphatic | IsoCyanate_SaturatedAliphatic |
| IsoCyanate | IsoCyanate_Aliphatic | IsoCyanate_UnsaturatedAliphatic |
| IsoCyanate | IsoCyanate_Aromatic | IsoCyanate_Aromatic |
| IsoCyanate | IsoCyanate_Heteroaromatic | IsoCyanate_Heteroaromatic |
| Boroxine | AromBoroxine | AromBoroxine |
| Boroxine | AliphaticBoroxine | AliphaticBoroxine |
| Boroxine | MixBoroxine | MixBoroxine |
| Boronate | Boronate_Aliphatic | Boronate_SaturatedAliphatic |
| Boronate | Boronate_Aliphatic | Boronate_UnsaturatedAliphatic |
| Boronate | Boronate_Aromatic | Boronate_Aromatic |
| Boronate | Boronate_Heteroaromatic | Boronate_Heteroaromatic |
| Boronate | PincerBoronate | PincerBoronate |
| Boronate | AromDiboronate | AromDiboronate |
| Boronate | AliphaticDiboronate | AliphaticDiboronate |
| Boronate | TrialkylBoronate | TrialkylBoronate |
| Boronate | TrifluoroBoronateAromatic | TrifluoroBoronateAromatic |
| Boronate | TrifluoroBoronateAliphatic | TrifluoroBoronateAliphatic |
| Boronic | Boronic_Aliphatic | Boronic_SaturatedAliphatic |
| Boronic | Boronic_Aliphatic | Boronic_UnsaturatedAliphatic |
| Boronic | Boronic_Aromatic | Boronic_Aromatic |
| Boronic | Boronic_Heteroaromatic | Boronic_Heteroaromatic |
| Boronic | BoronicCyclic | BoronicCyclic |
| Borane | AliphaticBorane | AliphaticBorane |
| Borane | AliphaticDiborane | AliphaticDiborane |
| Protecting | Fmoc | Fmoc |
| Protecting | Boc | Boc |
| Protecting | Pivalic | Pivalic |
| Alkene/MichaelAcceptor | AlkeneTerminal | AlkeneTerminal |
| Alkene/MichaelAcceptor | AlkeneNonTerminal | AlkeneNonTerminal |
| Thioether | ThioetherAliphaticCyclic | ThioetherAliphaticCyclic |
| Thioether | ThioetherMixCyclic | ThioetherMixCyclic |
| Thioether | ThioetherAromaticAcyclic | ThioetherAromaticAcyclic |
| Thioether | ThioetherAliphaticAcyclic | ThioetherAliphaticAcyclic |
| Thioether | ThioetherMixAcyclic | ThioetherMixAcyclic |
| Ether | EtherAromaticAcyclic | EtherAromaticAcyclic |
| Ether | EtherAliphaticCyclic | EtherAliphaticCyclic |
| Ether | EtherAliphaticAcyclic | EtherAliphaticAcyclic |
| Ether | EtherMixCyclic | EtherMixCyclic |
| Ether | EtherMixAcyclic | EtherMixAcyclic |
| Ketals | Ketals | Ketals |
| Ketals | Ketals | ThioKetals |
| Ketals | Acetal | Acetal |
| Ketals | Acetal | ThioAcetal |
| Sulfone | Sulfone | Sulfone |
| Alkyne | AlkyneTerminalAromatic | AlkyneTerminalAromatic |
| Alkyne | AlkyneTerminalAliphatic | AlkyneTerminalAliphatic |
| Alkyne | AlkyneNonTerminalAromatic | AlkyneNonTerminalAromatic |
| Alkyne | AlkyneNonTerminalAliphatic | AlkyneNonTerminalAliphatic |
| Alkyne | AlkyneNonTerminalMix | AlkyneNonTerminalMix |
| Sulphonamide | Sulphonamide | Sulphonamide0H |
| Sulphonamide | Sulphonamide | Sulphonamide1H |
| Sulphonamide | Sulphonamide | Sulphonamide2H |
| Thiocarbamate | Thiocarbamate | Thiocarbamate |
| Carbamate | Carbamate | Carbamate |
| Imide | Imide | Imide |
| TetraX | TetraX | TetraX |
| Phosphate | PhosphoricAcid | PhosphoricAcid |
| Phosphate | PhosphoricEster_Aliphatic | PhosphoricEster_SaturatedAliphatic |
| Phosphate | PhosphoricEster_Aliphatic | PhosphoricEster_UnsaturatedAliphatic |
| Phosphate | PhosphoricEster_Aromatic | PhosphoricEster_Aromatic |
| Phosphate | PhosphoricEster_Heteroaromatic | PhosphoricEster_Heteroaromatic |
| Phosphate | PhosphoricAmide_Aliphatic | PhosphoricAmide_Aliphatic |
| Phosphate | PhosphoricAmide_Aromatic | PhosphoricAmide_Aromatic |
| Phosphate | PhosphoricAmide_Mix | PhosphoricAmide_Mix |
| Sulfinate | Sulfinate | Sulfinate |
| Amide | Amide | Amide |
| Amide | Amide | Pyridone_likeNH |
| Oxime | Oxime | Oxime |
| Azide | Azide | Azide |
| Phenol | PhenolHeteroaromatic6membered | PhenolHeteroaromatic6membered |
| Phenol | PhenolHeteroaromatic5membered | PhenolHeteroaromatic5membered |
| Phenol | Phenol | Phenol |
| Thiophenol | ThiophenolHeteroaromatic6membered | ThiophenolHeteroaromatic6membered |
| Thiophenol | ThiophenolHeteroaromatic5membered | ThiophenolHeteroaromatic5membered |
| Thiophenol | Thiophenol | Thiophenol |
| Thiol | PrimaryThiolAromatic | PrimaryThiolAromatic |
| Thiol | PrimaryThiolAliphatic | PrimaryThiolAliphatic |
| Thiol | SecondaryThiolAromaticCyclic | SecondaryThiolAromaticCyclic |
| Thiol | SecondaryThiolAliphaticCyclic | SecondaryThiolAliphaticCyclic |
| Thiol | SecondaryThiolMixCyclic | SecondaryThiolMixCyclic |
| Thiol | SecondaryThiolAromaticAcyclic | SecondaryThiolAromaticAcyclic |
| Thiol | SecondaryThiolAliphaticAcyclic | SecondaryThiolAliphaticAcyclic |
| Thiol | SecondaryThiolMixAcyclic | SecondaryThiolMixAcyclic |
| Thiol | TertiaryThiolCyclic | TertiaryThiolCyclic |
| Thiol | TertiaryThiolAcyclic | TertiaryThiolAcyclic |
| Alcohol | PrimaryAlcoholAromatic | PrimaryAlcoholAromatic |
| Alcohol | PrimaryAlcoholAliphatic | PrimaryAlcoholAliphatic |
| Alcohol | SecondaryAlcoholAromaticCyclic | SecondaryAlcoholAromaticCyclic |
| Alcohol | SecondaryAlcoholAliphaticCyclic | SecondaryAlcoholAliphaticCyclic |
| Alcohol | SecondaryAlcoholMixCyclic | SecondaryAlcoholMixCyclic |
| Alcohol | SecondaryAlcoholAromaticAcyclic | SecondaryAlcoholAromaticAcyclic |
| Alcohol | SecondaryAlcoholAliphaticAcyclic | SecondaryAlcoholAliphaticAcyclic |
| Alcohol | SecondaryAlcoholMixAcyclic | SecondaryAlcoholMixAcyclic |
| Alcohol | TertiaryAlcoholCyclic | TertiaryAlcoholCyclic |
| Alcohol | TertiaryAlcoholAcyclic | TertiaryAlcoholAcyclic |
| Amidine | Amidine | Amidine |
| Urea | AromaticUrea | AromaticUrea |
| Urea | MixUrea | MixUrea |
| Urea | AliphaticUrea | AliphaticUrea |
| Urea | AromaticThiourea | AromaticThiourea |
| Urea | MixThiourea | MixThiourea |
| Urea | AliphaticUrea | AliphaticThioUrea |
| Urea | Hydantoin | Hydantoin |
| Phosphine | AromaticPhosphine | AromaticPhosphine |
| Phosphine | AliphaticPhosphine | AliphaticPhosphine |
| Phosphine | MixPhosphine | MixPhosphine |
| Phosphine | AromaticPhosphineOxyde | AromaticPhosphineOxyde |
| Phosphine | AliphaticPhosphineOxyde | AliphaticPhosphineOxyde |
| Phosphine | MixPhosphineOxyde | MixPhosphineOxyde |
| Sulfinylamine | SulfinylamineAromatic | SulfinylamineAromatic |
| Sulfinylamine | SulfinylamineAliphatic | SulfinylamineAliphatic |
| NitrogenHeterocycle | Heterocycle5_1N | Heterocycle5_1NH |
| NitrogenHeterocycle | Heterocycle5_1N | Heterocycle5_1NC |
| NitrogenHeterocycle | Heterocycle5_polyN | Heterocycle5_polyHetNH |
| NitrogenHeterocycle | Heterocycle5_polyN | Heterocycle5_polyHet |
| NitrogenHeterocycle | Heterocycle6_1N | Heterocycle6_1NC |
| NitrogenHeterocycle | Heterocycle6_1N | Heterocycle6_1N |
| NitrogenHeterocycle | Heterocycle6_polyN | Heterocycle6_polyHetNC |
| NitrogenHeterocycle | Heterocycle6_polyN | Heterocycle6_polyHet |
| OxygenHeterocycle | OxygenHeterocycle | Heterocycle5_O |
| SulfurHeterocycle | SulfurHeterocycle | Heterocycle5_S |
| Guanidine | Guanidine | Guanidine |
| Amonia | Amonia | Amonia |
| Amine | Benzyl_amine_primary | Benzylamine_primary |
| Amine | Benzyl_amine_primary | HeteroBenzylamine_primary |
| Amine | Amine_Aliphatic | Amine_Primary_SaturatedAliphatic |
| Amine | Amine_Aliphatic | Amine_Primary_UnsaturatedAliphatic |
| Amine | Amine_Aromatic | Amine_Primary_Phe |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het6 |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het5 |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het6Het5 |
| Amine | Amine_Heteroaromatic | Amine_Primary_PheHet5 |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het5Het6 |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het5Phe |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het5Het5 |
| Amine | Amine_Aromatic | Amine_Primary_PhePhe |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het6Phe |
| Amine | Amine_Heteroaromatic | Amine_Primary_PheHet6 |
| Amine | Amine_Heteroaromatic | Amine_Primary_Het6Het6 |
| Amine | Amine_Aliphatic | Amine_AcyclicSecondary_SaturatedAliphatic-SaturatedAliphatic |
| Amine | Amine_Aliphatic | Amine_AcyclicSecondary_SaturatedAliphatic-UnsaturatedAliphatic |
| Amine | Amine_Aromatic | Amine_AcyclicSecondary_SaturatedAliphatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_AcyclicSecondary_SaturatedAliphatic-Heteroaromatic |
| Amine | Amine_Aliphatic | Amine_AcyclicSecondary_UnsaturatedAliphatic-UnsaturatedAliphatic |
| Amine | Amine_Aromatic | Amine_AcyclicSecondary_UnsaturatedAliphatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_AcyclicSecondary_UnsaturatedAliphatic-Heteroaromatic |
| Amine | Amine_Aromatic | Amine_AcyclicSecondary_Aromatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_AcyclicSecondary_Aromatic-Heteroaromatic |
| Amine | Amine_Heteroaromatic | Amine_AcyclicSecondary_Heteroaromatic-Heteroaromatic |
| Amine | Amine_Aliphatic | Amine_CyclicSecondary_SaturatedAliphatic-SaturatedAliphatic |
| Amine | Amine_Aliphatic | Amine_CyclicSecondary_SaturatedAliphatic-UnsaturatedAliphatic |
| Amine | Amine_Aromatic | Amine_CyclicSecondary_SaturatedAliphatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_CyclicSecondary_SaturatedAliphatic-Heteroaromatic |
| Amine | Amine_Aliphatic | Amine_CyclicSecondary_UnsaturatedAliphatic-UnsaturatedAliphatic |
| Amine | Amine_Aromatic | Amine_CyclicSecondary_UnsaturatedAliphatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_CyclicSecondary_UnsaturatedAliphatic-Heteroaromatic |
| Amine | Amine_Aromatic | Amine_CyclicSecondary_Aromatic-Aromatic |
| Amine | Amine_Heteroaromatic | Amine_CyclicSecondary_Aromatic-Heteroaromatic |
| Amine | Amine_Heteroaromatic | Amine_CyclicSecondary_Heteroaromatic-Heteroaromatic |
| AmineT | AromaticTertiaryAmine | AromaticTertiaryAmine |
| AmineT | AliphaticTertiaryAmine | AliphaticTertiaryAmine |
| AmineT | MixTertiaryAmine | MixTertiaryAmine |
| Hydrazine | HydrazineTerminalAromatic | HydrazineTerminalAromatic |
| Hydrazine | HydrazineTerminalAliphatic | HydrazineTerminalAliphatic |
| Hydrazine | HydrazineTerminalCarbamoyl | HydrazineTerminalCarbamoyl |
| Hydrazine | HydrazineNonTerminalAromatic | HydrazineNonTerminalAromatic |
| Hydrazine | HydrazineNonTerminalAliphatic | HydrazineNonTerminalAliphatic |
| Hydrazine | HydrazineNonTerminalMix | HydrazineNonTerminalMix |
| HydroxyAmidine | HydroxyAmidine | HydroxyAmidine |
| Hydroxylamine | HydroxylamineAromatic | HydroxylamineAromatic |
| Hydroxylamine | HydroxylamineAliphatic | HydroxylamineAliphatic |
| Hydroxylamine | SubstitutedHydroxylamineAromatic | SubstitutedHydroxylamineAromatic |
| Hydroxylamine | SubstitutedHydroxylamineAliphatic | SubstitutedHydroxylamineAliphatic |
| Grignard | Grignard_Aliphatic | Grignard_SaturatedAliphatic |
| Grignard | Grignard_Aliphatic | Grignard_UnsaturatedAliphatic |
| Grignard | Grignard_Aromatic | Grignard_Aromatic |
| Grignard | Grignard_Heteroaromatic | Grignard_Heteroaromatic |
| Metals | Metals | Metals |
| Silicium | Silicium | Silicium1 |
| Silicium | Silicium | Silicium2 |
| Hydroxylamine | Hydroxylamine | Hydroxylamine |
| Halogen | Halogen | Halogen |
| Peroxyde | Peroxyde | Peroxyde |
| XPhosphorus | XPhosphorus | XPhosphorus |
