if __name__ == "__main__":

    from tmma.tmm import TMM

    # Define the frequency range, resolution and sound incidence
    treatment = TMM(fmin=10, fmax=5000, df=1, incidence="diffuse", incidence_angle=[0, 78, 1],
                    filename="example_slotted_resonator")

    # Define the layers - from top to bottom
    treatment.slotted_panel_layer(t=19, w=4, s=24, method="barrier")
    treatment.porous_layer(model="mac", t=50, sigma=27)
    treatment.air_layer(t=50)

    # Compute, plot and export data
    treatment.compute(rigid_backing=True, show_layers=True)
    treatment.plot(plots=["alpha"], save_fig=True, figsize=(7, 4))
    treatment.save2sheet(n_oct=3)
    treatment.save()
    bands, filtered_alpha = treatment.filter_alpha(view=True, n_oct=3)
